from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zipcode}"

class ShowRoom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    pic=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    showroom = models.ForeignKey(ShowRoom, on_delete=models.CASCADE)
    pic=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    pic=models.ImageField(null=True, blank=True)
    showroom = models.ForeignKey(ShowRoom, on_delete=models.CASCADE, null=True, default=None, blank=True)


    def __str__(self):
        return f"{self.name}, {self.showroom}"

class Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    showroom = models.ForeignKey(ShowRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Engine(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.customer} {self.car}"


class Car(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    VIN = models.CharField(max_length=17)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()
    pic = models.ImageField(null=True, blank=True)
    showroom_purchased = models.ForeignKey(ShowRoom, on_delete=models.SET_NULL, null=True, blank=True)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return f"{self.model.name}, {self.showroom_purchased}"