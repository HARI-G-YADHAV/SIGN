from django.db import models

# Create your models here.


class UploadedCSV(models.Model):
    status = models.CharField(max_length=10)
    RegNo = models.CharField(max_length=15)

    def __str__(self):
        return self.RegNo
    
