""" This file contains the serializers for the Patient model. """
from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Patient model.

    This serializer converts Patient model instances into various formats
    such as JSON or XML and vice versa.
    It includes all fields of the Patient model.

    Attributes:
        Meta (class): Meta options for the serializer.
            model (Patient): The model that is being serialized.
            fields (str): Specifies that all fields in the model should be
                included in the serialization.
    """
    class Meta:
        """
        Meta class to specify the model and fields to be used in the
        serializer.

        Attributes:
            model (type): The model class that this serializer will be
                based on.
            fields (str): A special value '__all__' indicating that all fields
                in the model should be included in the serializer.
        """
        model = Patient
        fields = '__all__'
