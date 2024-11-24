from django.contrib import admin
from .models import Client, Car, Repair

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'account_number', 'phone_number', 'contact_person', 'address')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_price', 'client')

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'car', 'repair_type', 'hourly_rate', 'discount', 'repair_hours')
