from rest_framework import filters,generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import TodoList
from .models import TodoItem
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import (
    TodoItemCreateSerializer,
    TodoListSerializer,
    TodoItemSerializer,
    TodoItemStatusSerializer
)

User = get_user_model()

class TodoListListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_public']
    search_fields = ['title', 'description']

    def get_queryset(self):
        user = self.request.user
        return TodoList.objects.filter(owner=user) | TodoList.objects.filter(is_public=True)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return TodoList.objects.filter(owner=user)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class TodoListItemListView(generics.ListCreateAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']

    def get_queryset(self):
        todo_list_id = self.kwargs['id']
        todo_list = get_object_or_404(TodoList, id=todo_list_id)
        if todo_list.owner != self.request.user and not todo_list.is_public:
            return TodoItem.objects.none()
        return TodoItem.objects.filter(todo_list=todo_list)

    def perform_create(self, serializer):
        todo_list_id = self.kwargs['id']
        todo_list = get_object_or_404(TodoList, id=todo_list_id)
        if todo_list.owner != self.request.user:
            raise permissions.PermissionDenied("You don't have permission to add items to this list")
        serializer.save(todo_list=todo_list)


class TodoItemListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list__owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TodoItemCreateSerializer
        return TodoItemSerializer


class TodoItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list__owner=self.request.user)


class TodoItemStatusUpdateView(generics.UpdateAPIView):
    serializer_class = TodoItemStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list__owner=self.request.user)


class TodoItemCompleteView(generics.GenericAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list__owner=self.request.user)

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'completed'
        instance.save()
        return Response(self.get_serializer(instance).data)


class TodoItemStartView(generics.GenericAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list__owner=self.request.user)

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'in_progress'
        instance.save()
        return Response(self.get_serializer(instance).data)
