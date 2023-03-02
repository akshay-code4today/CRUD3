from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['Vehicle_Number','Vehicle_Type','Vehicle_Model','Vehicle_Description']
