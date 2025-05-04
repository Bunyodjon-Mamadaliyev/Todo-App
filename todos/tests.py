from django.test import TestCase
from django.contrib.auth.models import User
from tags.models import Tag
from .models import TodoList, TodoItem

class TodoListModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.tag = Tag.objects.create(name="Urgent", color="#FF0000")
        self.todo_list = TodoList.objects.create(
            title="My Todo List",
            owner=self.user,
            is_public=True
        )

    def test_todo_list_creation(self):
        todo_list = self.todo_list
        self.assertEqual(todo_list.title, "My Todo List")
        self.assertEqual(todo_list.owner, self.user)
        self.assertTrue(todo_list.is_public)

    def test_todo_list_str_method(self):
        todo_list = self.todo_list
        self.assertEqual(str(todo_list), "My Todo List")


class TodoItemModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.tag = Tag.objects.create(name="Urgent", color="#FF0000")
        self.todo_list = TodoList.objects.create(
            title="My Todo List",
            owner=self.user,
            is_public=True
        )
        self.todo_item = TodoItem.objects.create(
            todo_list=self.todo_list,
            title="First Todo Item",
            priority=1,
            status='pending'
        )

    def test_todo_item_creation(self):
        todo_item = self.todo_item
        self.assertEqual(todo_item.title, "First Todo Item")
        self.assertEqual(todo_item.priority, 1)
        self.assertEqual(todo_item.status, 'pending')
        self.assertEqual(todo_item.todo_list, self.todo_list)

    def test_todo_item_str_method(self):
        todo_item = self.todo_item
        self.assertEqual(str(todo_item), "First Todo Item")

    def test_todo_item_tags(self):
        self.todo_item.tags.add(self.tag)
        self.assertIn(self.tag, self.todo_item.tags.all())

    def test_priority_choices(self):
        todo_item = TodoItem.objects.create(
            todo_list=self.todo_list,
            title="Second Todo Item",
            priority=2,
            status='pending'
        )
        self.assertEqual(todo_item.priority, 2)

    def test_status_choices(self):
        todo_item = TodoItem.objects.create(
            todo_list=self.todo_list,
            title="Third Todo Item",
            priority=3,
            status='completed'
        )
        self.assertEqual(todo_item.status, 'completed')
