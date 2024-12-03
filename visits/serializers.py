""" This file contains the serializers for the visits app. """
from rest_framework import serializers
from .models import Visit


class VisitSerializer(serializers.ModelSerializer):
    """
    Serializer for the Visit model.

    This serializer converts Visit model instances into JSON format
    and vice versa.
    It includes all fields of the Visit model.

    Attributes:
        Meta:
            model (Visit): The model that is being serialized.
            fields (str): Specifies that all fields in the model should be
            included in the serialization.
    """
    class Meta:
        """
        Meta class to specify the model and fields to be used in the
        serializer.

        Attributes:
            model (Visit): The model that the serializer will be based on.
            fields (str): Specifies that all fields in the model should be
            included in the serializer.
        """
        model = Visit
        fields = '__all__'
