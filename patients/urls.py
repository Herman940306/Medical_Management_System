""" URL Configuration for patients app """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('create/', views.patient_create, name='patient_create'),
    path('update/<int:pk>/', views.patient_update, name='patient_update'),
    path('delete/<int:pk>/', views.patient_delete, name='patient_delete'),
]
