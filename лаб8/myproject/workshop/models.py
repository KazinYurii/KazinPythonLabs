

from django.db import models

class Client(models.Model):
    company_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    contact_person = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()

    def str(self):
        return self.company_name


class Car(models.Model):
    car_brand = models.CharField(max_length=50)
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def str(self):
        return f"{self.car_brand} - {self.client.company_name}"


class Repair(models.Model):
    REPAIR_TYPES = [
        ('гарантійний', 'Гарантійний'),
        ('плановий', 'Плановий'),
        ('капітальний', 'Капітальний'),
    ]

    start_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    repair_type = models.CharField(max_length=20, choices=REPAIR_TYPES)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=1)
    repair_hours = models.PositiveIntegerField()

    def str(self):
        return f"Repair #{self.id} for {self.car.car_brand}"
