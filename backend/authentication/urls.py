# authentication/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views
from .views import sign_up, sign_in


urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
]
