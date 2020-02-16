from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='raazesh',
            email='raazesh@email.com',
            password='12345'
        )
        self.assertEqual(user.uname, 'raazesh')
        self.assertEqual(user.email, 'raazesh@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='superuser',
            email='superuser@email.com',
            password='12435'
        )
        self.assertEqual(user.uname, 'superuser')
        self.assertEqual(user.email, 'superuser@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
