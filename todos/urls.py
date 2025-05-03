from django.urls import path
from .views import (
    TodoListListCreateView,
    TodoListRetrieveUpdateDestroyView,
    TodoListItemListView,
    TodoItemListCreateView,
    TodoItemRetrieveUpdateDestroyView,
    TodoItemStatusUpdateView,
    TodoItemCompleteView,
    TodoItemStartView,
)

urlpatterns = [
    path('todo-lists/', TodoListListCreateView.as_view(), name='todo-list-list-create'),
    path('todo-lists/<uuid:id>/', TodoListRetrieveUpdateDestroyView.as_view(), name='todo-list-retrieve-update-destroy'),
    path('todo-lists/<uuid:id>/items/', TodoListItemListView.as_view(), name='todo-list-items'),

    path('todo-items/', TodoItemListCreateView.as_view()),
    path('todo-items/<uuid:id>/', TodoItemRetrieveUpdateDestroyView.as_view()),
    path('todo-items/<uuid:id>/status/', TodoItemStatusUpdateView.as_view()),
    path('todo-items/<uuid:id>/complete/', TodoItemCompleteView.as_view()),
    path('todo-items/<uuid:id>/start/', TodoItemStartView.as_view()),
]

