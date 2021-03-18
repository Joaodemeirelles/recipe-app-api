from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ """
        email = "jota@gmail.com"
        password = "aaaaab"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalize(self):
        """Test"""
        email = 'teste@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password="123452515"
        )

        self.assertEqual(user.email, email.lower())

    def test_create_superuser(self):
        """ """
        email = "teste@gmail.com"
        user = get_user_model().objects.create_superuser(
            email=email,
            password = "estaaaraedada"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
