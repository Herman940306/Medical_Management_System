""" This file contains the views for the visits app. """
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Visit
from .serializers import VisitSerializer
from .forms import VisitForm


class VisitViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing visit instances.

    Attributes:
        queryset (QuerySet): The queryset that retrieves all Visit objects.
        serializer_class (Serializer): The serializer class used to validate
        and serialize Visit objects.
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


def visit_list(request):
    """
    Handles the request to display a list of all visits.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying the list of visits.
    """
    visits = Visit.objects.all()
    return render(request, 'visits/visit_list.html', {'visits': visits})


def visit_create(request):
    """
    Handle the creation of a new visit.

    If the request method is POST, validate and save the form data to create
    a new visit.
    If the form is valid, redirect to the visit list page.
    If the request method is not POST, display an empty visit form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered visit form or
        a redirect to the visit list.
    """
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visit_list')
    else:
        form = VisitForm()
    return render(request, 'visits/visit_form.html', {'form': form})


def visit_update(request, pk):
    """
    Update an existing visit instance.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the visit to be updated.

    Returns:
        HttpResponse: The response object containing the rendered template or a
        redirect to the visit list.

    This view handles both GET and POST requests. On a GET request, it displays
    a form pre-filled with the visit's current data.
    On a POST request, it processes the form data, validates it, and saves the
    updated visit if the form is valid.
    """
    visit = Visit.objects.get(pk=pk)
    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('visit_list')
    else:
        form = VisitForm(instance=visit)
    return render(request, 'visits/visit_form.html', {'form': form})


def visit_delete(request, pk):
    """
    Handle the deletion of a visit.

    This view handles the deletion of a visit instance identified by its
    primary key (pk).
    If the request method is POST, the visit instance is deleted and the user
    is redirected
    to the visit list page. If the request method is not POST, a confirmation
    page is rendered.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the visit instance to be deleted.

    Returns:
        HttpResponse: A redirect to the visit list page if the request method
        is POST.
                      Otherwise, renders the visit confirmation delete page.
    """
    visit = Visit.objects.get(pk=pk)
    if request.method == 'POST':
        visit.delete()
        return redirect('visit_list')
    return render(request, 'visits/visit_confirm_delete.html',
                  {'visit': visit})

# Create your views here.
