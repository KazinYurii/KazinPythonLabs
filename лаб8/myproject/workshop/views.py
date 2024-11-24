from django.shortcuts import render
from .models import Client, Car, Repair

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'workshop/client_list.html', {'clients': clients})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'workshop/car_list.html', {'cars': cars})

def repair_list(request):
    repairs = Repair.objects.all()
    return render(request, 'workshop/repair_list.html', {'repairs': repairs})
