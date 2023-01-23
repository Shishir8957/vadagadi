from django.db import models
from django.utils.translation import gettext as _

class FuleType(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
class Transmission(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
class vehicleType(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
# class Product(models.Model):
#     name = models.CharField(_("Make"),max_length=200)
#     model = models.CharField(_("Model"),max_length=200)
#     price = models.BigIntegerField(_("Price"))
#     year = models.DateField(_("Year"),auto_now=True)
#     kilometer = models.BigIntegerField(_("Kilometer"))
#     fuletype = models.CharField(_("Fuel Type"),max_length=200)
#     Transmission = models.CharField(_("Transmission"),max_length=100)
#     color = models.CharField(_("Color"),max_length=200)
#     engine = models.CharField(_("Engine"),max_length=200)
#     maxPower = models.CharField(_("Max Power"),max_length=200)
#     maxTorque = models.CharField(_("Max Torque"),max_length=200)
#     Drivetrain = models.CharField(_("Drivetrain"),max_length=200)
#     length = models.IntegerField(_("Length"))
#     width = models.IntegerField(_("Width"))
#     height = models.IntegerField(_("Height"))
#     fuleTankSize = models.IntegerField(_("Seating Capacity"))
#     vehicleType = models.CharField(_("vehicle_type"),max_length=200)
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    kilometer = models.CharField(max_length=200)
    fuletype = models.CharField(max_length=200)
    Transmission = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    maxPower = models.CharField(max_length=200)
    maxTorque = models.CharField(max_length=200)
    Drivetrain = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    width = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    seatingCapacity = models.CharField(max_length=200)
    fuleTankSize = models.CharField(max_length=200)
    vehicleType = models.CharField(max_length=200)


