""" This module contains the UserSerializer class. """
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer is a ModelSerializer for the User model.

    This serializer automatically generates fields for all the attributes
    of the User model.

    Attributes:
        Meta (class): A nested class that defines the metadata options
        for the serializer.
            model (User): The model that is being serialized.
            fields (str): Specifies that all fields in the model should be
            included in the serialization.
    """
    class Meta:
        """
        Meta class for the User serializer.

        Attributes:
            model (django.db.models.Model): The model that is being serialized.
            fields (str or list): Specifies which fields should be included
                                  in the serialization. In this case, all
                                  fields of the model are included.
        """
        model = User
        fields = '__all__'
