from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Contact)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','email','contact_number','less_message')
    def less_message(sef,obj):
        return obj.message[:100]