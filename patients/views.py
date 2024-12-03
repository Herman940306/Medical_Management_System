""" This file contains the views for the patients app. """
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
from .forms import PatientForm


class PatientViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patient instances.

    Attributes:
        queryset (QuerySet): The queryset that retrieves all patient instances.
        serializer_class (Serializer): The serializer class used to validate
                                       and serialize patient instances.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


def patient_list(request):
    """
    View function to display a list of patients.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying the list of patients.
    """
    patients = Patient.objects.all()
    return render(
        request, 'patients/patient_list.html', {'patients': patients}
    )


def patient_create(request):
    """
    Handle the creation of a new patient record.

    If the request method is POST, validate and save the patient form.
    If the form is valid, redirect to the patient list view.
    If the request method is not POST, display an empty patient form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered patient form template or a redirect to the
        patient list.
    """
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})


def patient_update(request, pk):
    """
    Update an existing patient's information.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the patient to be updated.

    Returns:
        HttpResponse: The response object containing the rendered template or
        a redirect to the patient list.

    This view handles both GET and POST requests. On a GET request, it displays
    a form pre-filled with the patient's
    current information. On a POST request, it validates and saves the updated
    patient information, then redirects
    to the patient list.
    """
    patient = Patient.objects.get(pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {'form': form})


def patient_delete(request, pk):
    """
    Handle the deletion of a patient record.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the patient to be deleted.

    Returns:
        HttpResponse: Redirects to the patient list if the request method is
        POST.
        Otherwise, renders the patient confirmation delete page.
    """
    patient = Patient.objects.get(pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients/patient_confirm_delete.html',
                  {'patient': patient})
