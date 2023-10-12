from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import redirect

User = get_user_model()
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return redirect("http://127.0.0.1:8000/admin/upload/uploadedcsv/")


