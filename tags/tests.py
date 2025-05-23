from django.test import TestCase
from .models import Tag
import uuid


class TagModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(
            name="Technology",
            color="#0000FF"
        )

    def test_tag_creation(self):
        tag = self.tag
        self.assertEqual(tag.name, "Technology")
        self.assertEqual(tag.color, "#0000FF")
        self.assertIsNotNone(tag.created_at)

    def test_tag_str_method(self):
        tag = self.tag
        self.assertEqual(str(tag), "Technology")

    def test_unique_name_constraint(self):
        with self.assertRaises(Exception):
            Tag.objects.create(name="Technology", color="#FF0000")

    def test_tag_field_types(self):
        tag = self.tag
        self.assertIsInstance(tag.id, uuid.UUID)
        self.assertIsInstance(tag.name, str)
        self.assertIsInstance(tag.color, str)
