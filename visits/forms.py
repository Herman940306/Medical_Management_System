""" This file contains the form for the Visit model. """
from django import forms
from .models import Visit


class VisitForm(forms.ModelForm):
    """
    VisitForm is a ModelForm for creating and updating Visit instances.

    Fields:
        - patient: The patient associated with the visit.
        - visit_date: The date of the visit.
        - reason: The reason for the visit.
        - doctor: The doctor attending the visit.

    Meta:
        - model: The model associated with this form (Visit).
        - fields: The fields to be included in the form.
    """
    class Meta:
        """
        Meta class for the Visit form.

        Attributes:
            model (Model): The model associated with the form, which is Visit.
            fields (list): The list of fields to be included in the form.
                           It includes 'patient', 'visit_date', 'reason',
                           and 'doctor'.
        """
        model = Visit
        fields = ['patient', 'visit_date', 'reason', 'doctor']
