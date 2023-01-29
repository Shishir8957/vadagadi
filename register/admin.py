from django.contrib import admin
from .models import *

# Register your models here.
class randomStringAdmin(admin.ModelAdmin):
    list_display = ('user','random')
admin.site.register(randomString,randomStringAdmin)
