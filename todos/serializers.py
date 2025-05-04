from rest_framework import serializers
from .models import TodoItem, TodoList
from tags.models import Tag
from django.contrib.auth import get_user_model

User = get_user_model()

class TodoListSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    progress = serializers.SerializerMethodField()
    item_count = serializers.SerializerMethodField()

    class Meta:
        model = TodoList
        fields = [
            'id', 'title', 'description', 'owner', 'is_public',
            'created_at', 'updated_at', 'progress', 'item_count'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'progress', 'item_count']

    def get_progress(self, obj):
        total_items = obj.items.count()
        if total_items == 0:
            return 0
        completed_items = obj.items.filter(status='completed').count()
        return int((completed_items / total_items) * 100)

    def get_item_count(self, obj):
        return obj.items.count()

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long")
        return value


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        ref_name = 'TodoTagSerializer'

class TodoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = TodoItem
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']


class TodoItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']


class TodoItemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['status']
