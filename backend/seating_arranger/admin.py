from django.contrib import admin

# Register your models here.
from .models import RoomDetails

admin.site.register(RoomDetails)
class RoomDetails(admin.ModelAdmin):
    list_display = ('rows', 'columns','roomno','noofbenches','benchstrength')




