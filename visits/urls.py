""" URL Configuration for visits app """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.visit_list, name='visit_list'),
    path('create/', views.visit_create, name='visit_create'),
    path('update/<int:pk>/', views.visit_update, name='visit_update'),
    path('delete/<int:pk>/', views.visit_delete, name='visit_delete'),
]
