from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response

User = get_user_model()
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")


