"""Models for the visits app."""
from django.db import models
from patients.models import Patient


class Visit(models.Model):
    """
    Represents a medical visit.

    Attributes:
        patient (ForeignKey): A reference to the patient associated
        with the visit.
        visit_date (DateField): The date of the visit.
        reason (TextField): The reason for the visit.
        doctor (CharField): The name of the doctor who conducted the visit.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_date = models.DateField()
    reason = models.TextField()
    doctor = models.CharField(max_length=100)
