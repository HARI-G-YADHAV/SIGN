from django.db import models
from upload.models import UploadedCSV

# Create your models here.
class RoomDetails(models.Model):
    roomno=models.IntegerField()
    rows=models.IntegerField()
    columns=models.IntegerField()
    noofbenches=models.IntegerField()
    benchstrength=models.IntegerField()

    def __str__(self):
        return f"{self.roomno}"
