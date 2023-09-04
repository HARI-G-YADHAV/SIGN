from django.shortcuts import render,redirect


# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedCSV

@csrf_exempt  # Use this decorator for simplicity. You should use proper CSRF protection in production.
def upload_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']

        # Create a new UploadedCSV instance and save it
        uploaded_csv = UploadedCSV(file=csv_file)
        uploaded_csv.save()


        # Return a JSON response with a success message
        response_data = {'message': 'CSV file uploaded successfully'}
        return JsonResponse(response_data)

    # Handle other cases (e.g., GET request or no file uploaded)
    response_data = {'error': 'Invalid request'}
    return JsonResponse(response_data, status=400)
