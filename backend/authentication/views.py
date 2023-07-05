# authentication/views.py

from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response

User = get_user_model()

@api_view(['POST'])
def sign_up(request):
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')

    if not email or not password or not first_name or not last_name:
        return Response({'error': 'Missing required fields'}, status=400)

    try:
        User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        return Response({'message': 'User created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
def sign_in(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Missing email or password'}, status=400)

    user = User.objects.filter(email=email).first()

    if not user or not user.check_password(password):
        return Response({'error': 'Invalid email or password'}, status=401)

    # Here, you can generate and return an authentication token if you're using token-based authentication.
    # Alternatively, you can use session-based authentication.

    return Response({'message': 'Sign-in successful'}, status=200)
