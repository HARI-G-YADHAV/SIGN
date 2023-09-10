from django.contrib import admin

# Register your models here.
from .models import UploadedCSV

admin.site.register(UploadedCSV)
class UploadedCSVAdmin(admin.ModelAdmin):
    list_display = (' status', 'RegNo')
