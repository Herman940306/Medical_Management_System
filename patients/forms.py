""" This file contains the form for the Patient model. """
from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    """
    A form for creating and updating Patient instances.

    This form is based on the Patient model and includes the following fields:
    - name: The name of the patient.
    - address: The address of the patient.
    - date_of_birth: The date of birth of the patient.
    """
    class Meta:
        """
        Meta class to specify the model and fields to be used in the form.

        Attributes:
            model (Model): The model associated with the form.
            fields (list): List of fields to include in the form.
        """
        model = Patient
        fields = ['name', 'address', 'date_of_birth']
