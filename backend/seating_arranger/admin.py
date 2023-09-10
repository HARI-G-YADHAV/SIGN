from django.contrib import admin

# Register your models here.
from .models import classCSV

admin.site.register(classCSV)
class classCSV(admin.ModelAdmin):
    list_display = ('row', 'column','name')
