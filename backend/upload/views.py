# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedCSV
from .forms import CSVUploadForm
import csv
import io

@csrf_exempt
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)

        if form.is_valid():
            # Create a new UploadedCSV instance and save it
            handle_csv_file(request.FILES['csv_file'])

            # Return a JSON response with a success message
            response_data = {'message': 'CSV file uploaded successfully'}
            return JsonResponse(response_data)
        else:
            response_data = {'error': 'Invalid form data'}
            return JsonResponse(response_data, status=400)

    else:
        form = CSVUploadForm()
        # Handle other cases (e.g., GET request or no file uploaded)
        response_data = {'error': 'Invalid request'}
        return JsonResponse(response_data, status=400)

def handle_csv_file(csv_file):
    csv_data = csv_file.read().decode('utf-8')
    reader = csv.reader(io.StringIO(csv_data))
    UploadedCSV.objects.all().delete()
    for row in reader:
        status = row[0]  # Assuming the status is in the first column
        reg_no = row[1]  # Assuming the RegNo is in the second column

        details = UploadedCSV(status=status, RegNo=reg_no)
        details.save()
