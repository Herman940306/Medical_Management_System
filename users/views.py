""" This file contains the views for the users app. """
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .forms import UserForm, LoginForm


class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet is a viewset for handling user-related operations.

    This viewset provides the following actions:
    - list: Retrieve a list of all users.
    - create: Create a new user.
    - retrieve: Retrieve a specific user by ID.
    - update: Update an existing user.
    - partial_update: Partially update an existing user.
    - destroy: Delete a user.

    Attributes:
        queryset (QuerySet): The queryset that retrieves all users.
        serializer_class (Serializer): The serializer class used to serialize
        user data.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


def user_list(request):
    """
    View function to display a list of users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying the list of users.
    """
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_create(request):
    """
    Handle the creation of a new user.

    This view function handles both the GET and POST requests for creating a
    new user.
    If the request method is POST, it processes the submitted form data.
    If the form is valid, it saves the new user and redirects to the user list
    page.
    If the request method is GET,
    it displays an empty user creation form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered user creation
        form or a redirect to the user list page.
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})


def user_update(request, pk):
    """
    Update an existing user.

    This view handles the updating of an existing user identified by the
    primary key (pk).
    If the request method is POST, it attempts to update the user with the
    provided data.
    If the form is valid, the user is saved and the view redirects to the
    user list.
    If the request method is not POST, it displays the user update form
    with the current user data.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the user to be updated.

    Returns:
        HttpResponse: The rendered user update form or a redirect to the user
        list.
    """
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})


def user_delete(request, pk):
    """
    Handle the deletion of a user.

    This view retrieves a user by their primary key (pk) and, if the request
    method is POST,
    deletes the user and redirects to the user list page. If the request method
    is not POST,
    it renders a confirmation page for the user deletion.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the user to be deleted.

    Returns:
        HttpResponse: A redirect to the user list page if the user is deleted,
        or a rendered
                      confirmation page if the request method is not POST.
    """
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})


def login_view(request):
    """
    Handles the user login view.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered login page.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home page or dashboard
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
