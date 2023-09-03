# authentication/views.py

from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import IntegrityError

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

        user = User.objects.filter(username=username).first()

        if not user or not user.check_password(password):
            return JsonResponse({'message': 'Invalid email or password'}, status=401)
        message = 'Sign-in successful'

        return JsonResponse({'message1': message, 'user_id': user.id}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

