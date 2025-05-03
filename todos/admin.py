from django.contrib import admin
from .models import TodoList, TodoItem

class TodoItemInline(admin.TabularInline):
    model = TodoItem
    extra = 1
    show_change_link = True
    autocomplete_fields = ['tags']

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_public', 'created_at', 'updated_at')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ['owner']
    inlines = [TodoItemInline]

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'todo_list', 'priority', 'status', 'due_date', 'created_at')
    list_filter = ('priority', 'status', 'due_date', 'created_at')
    search_fields = ('title', 'description', 'todo_list__title')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ['todo_list', 'tags']
