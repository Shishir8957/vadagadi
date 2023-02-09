from django.db import models

# Create your models here.
class privacyPolicy(models.Model):
    content = models.TextField(blank=True)
    def __str__(self):
        return 'privacyPolicy'