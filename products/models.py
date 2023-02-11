from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils.timezone import now

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
    ratings = models.CharField(max_length=200)
    booked = models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.name+' '+'Model: '+ self.model

class Booking(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    starting = models.DateField(null=True)
    ending = models.DateField(null=True)
    pickupTime = models.TimeField(null=True)
    total_days = models.IntegerField(default=0,null=True)
    cost_per_day = models.BigIntegerField(default=0,null=True)
    verified = models.BooleanField(default=False)
    delivery_status = models.BooleanField(default=False)
    driverStatus = models.BooleanField(default=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

class PaymentComplete(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
   product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
   amount = models.IntegerField(default=0,null=True)
   payment_type = models.CharField(max_length=200,null=True)
   payment = models.BooleanField(default=False)

class Comment(models.Model):
    sno = models.AutoField(primary_key= True)
    comment = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:15]+"... "+ "by " + self.user.username
    
# class Promise(models):
#     title = models.CharField(max_length=300)
#     description = models.TextField(blank=True)
#     made_on = models.DateField()