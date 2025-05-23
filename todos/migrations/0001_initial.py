# Generated by Django 4.2 on 2025-05-02 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_lists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('priority', models.IntegerField(choices=[(1, 'Yuqori'), (2, 'O‘rta'), (3, 'Past')])),
                ('status', models.CharField(choices=[('pending', 'Kutilmoqda'), ('in_progress', 'Jarayonda'), ('completed', 'Bajarildi'), ('cancelled', 'Bekor qilingan')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='todo_items', to='tags.tag')),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='todos.todolist')),
            ],
        ),
    ]
