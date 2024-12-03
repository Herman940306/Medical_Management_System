""" This module contains the UserForm class used
to create and update User instances. """
from django import forms
from .models import User


class UserForm(forms.ModelForm):
    """
    A form for creating and updating User instances.

    This form is based on the User model and includes the following fields:
    - username: The username of the user.
    - password: The password for the user.
    - role: The role assigned to the user.

    Attributes:
        Meta (class): A class used to specify the model and fields for the
        form.
    """
    class Meta:
        """
        Meta class to specify the model and fields to be used in the form.

        Attributes:
            model (User): The model that the form is based on.
            fields (list): The list of fields to include in the form.
        """
        model = User
        fields = ['username', 'password', 'role']


class LoginForm(forms.Form):
    """
    LoginForm is a Django form used for user authentication.

    Attributes:
        username (CharField): A field for the user's username with a maximum
        length of 100 characters.
        password (CharField): A field for the user's password, rendered as a
        password input widget.
    """
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
