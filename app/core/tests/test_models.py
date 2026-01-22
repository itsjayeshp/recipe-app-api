"""
Test for models
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        sample_email = [
            ("test1@EXAMPLE.COM", "test1@example.com"),
            ("Test2@example.com", "Test2@example.com"),
            ("TEST3@Example.com", "TEST3@example.com"),
            ("test4@example.COM", "test4@example.com"),
        ]
        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, "testpass123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating user without email raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "testpass123")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com", "testpass123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful"""
        user = get_user_model().objects.create_user(
            "test@example.com", "testpass123"
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title="Sample recipe name",
            time_minutes=5,
            price=Decimal("5.99"),
            description="Sample recipe description",
        )

        self.assertEqual(str(recipe), recipe.title)
