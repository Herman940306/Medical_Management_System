# medical_management_system/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
