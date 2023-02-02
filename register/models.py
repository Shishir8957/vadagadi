from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


class randomString(models.Model):
    random = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.random

class VerifyUser(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    profile = models.ImageField(upload_to='images/',default='images/Group_1.png')
    # userDocument = models.ImageField(null=True,blank=True)