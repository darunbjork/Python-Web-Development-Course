# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):

    def test_user_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username="testuser", password="password123")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("password123"))

    def test_superuser_creation(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username="adminuser", password="adminpassword123")
        self.assertEqual(admin_user.username, "adminuser")
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)
