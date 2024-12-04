
"""
This module contains the models for the users app.
"""

from django.db import models


class User(models.Model):
    """
    User model representing a user in the medical management system.

    Attributes:
        username (str): The unique username of the user.
        password (str): The password for the user.
        role (str): The role of the user within the system.
        email (str): The email address of the user.
    """
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def is_role(self, role):  # check if the user has a specific role
        """
        Check if the user has a specific role.

        Args:
            role (str): The role to check.

        Returns:
            bool: True if the user has the specified role, False otherwise.
        """
        return self.role == role
