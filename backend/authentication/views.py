# authentication/views.py

from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login


User = get_user_model()

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        try:
            # Retrieve the JSON data from the request body
            data = json.loads(request.body)
        except json.JSONDecodeError as e:
            # Return an error response if the JSON data is invalid
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        email = data.get('email')
        password = data.get('password')
        username = data.get('username')

        if not email or not password or not username:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        try:
            user = User.objects.create_user(email=email, password=password, username=username)
            return JsonResponse({'message': 'User created successfully', 'user_id': user.id}, status=201)
        except IntegrityError as e:
            return JsonResponse({'success': False, 'message': 'Username already exists'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        if not username or not password:
            return JsonResponse({'message': 'Missing email or password'}, status=400)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            is_admin = user.is_superuser
            return JsonResponse({'token': token.key, 'user_id': user.id, 'message': '','is_admin': is_admin,}, status=200)
        else:
            return JsonResponse({'message': 'Invalid email or password'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
