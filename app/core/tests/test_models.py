from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@testemail.com'
        display_name = 'My Display Name'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
        email = email,
        display_name = display_name,
        password = 'TestPass123'
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.display_name, display_name)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
    	"""Test the email for a new user is normalized"""
    	email = 'test@TESTEMAIL.com'
    	user = get_user_model().objects.create_user(email, 'TestPass123')

    	self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'TestPass123')


    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'superuser@testemail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)