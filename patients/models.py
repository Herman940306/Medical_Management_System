"""Models for the patients app.
    """
from django.db import models


class Patient(models.Model):
    """
    Represents a patient in the medical management system.

    Attributes:
        name (str): The name of the patient.
        address (str): The address of the patient.
        date_of_birth (date): The date of birth of the patient.
    """
    name = models.CharField(max_length=100)
    address = models.TextField()
    date_of_birth = models.DateField()
