from django.db import models

# Create your models here.
class classCSV(models.Model):
    row = models.CharField(max_length=10)
    column = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name