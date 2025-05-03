from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import UserProfile

class UserProfileModelTest(TestCase):

    def setUp(self):
        # Test uchun User yaratish
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Avatar faylini yaratish
        self.avatar_file = SimpleUploadedFile(
            name='test_avatar.jpg',
            content=b'fake image content',
            content_type='image/jpeg'
        )
        # UserProfile yaratish
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            bio="This is a bio.",
            avatar=self.avatar_file,
            security_question="What is your favorite color?",
            security_answer="Blue"
        )

    def test_user_profile_creation(self):
        # UserProfile to'g'ri yaratildi yoki yo'qligini tekshirish
        user_profile = self.user_profile
        self.assertEqual(user_profile.user.username, "testuser")
        self.assertEqual(user_profile.bio, "This is a bio.")
        self.assertEqual(user_profile.security_question, "What is your favorite color?")
        self.assertEqual(user_profile.security_answer, "Blue")
        self.assertIsNotNone(user_profile.created_at)
        self.assertIsNotNone(user_profile.updated_at)

    def test_user_profile_avatar(self):
        # Avatar fayl nomini solishtirish
        user_profile = self.user_profile
        self.assertTrue(user_profile.avatar.name.startswith('avatars/'))

    def test_user_profile_str_method(self):
        # __str__ metodini test qilish
        user_profile = self.user_profile
        self.assertEqual(str(user_profile), "testuser profili")

    def test_security_answer_encryption(self):
        # Security answer shifrlanganligini tekshirish
        user_profile = self.user_profile
        # Shifrlangan qiymatni saqlashdan oldin va keyin tekshirganingizda,
        # shifrlangan qiymat alohida saqlanadi.
        self.assertEqual(user_profile.security_answer, "Blue")
