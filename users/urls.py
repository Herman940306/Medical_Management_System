""" URL patterns for users """
from django.urls import path
from . import views
from .views import login_view


urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('update/<int:pk>/', views.user_update, name='user_update'),
    path('delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('login/', login_view, name='login'),
]
