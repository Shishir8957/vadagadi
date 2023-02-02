from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'
class CustomizeUserAdmin(UserAdmin):
    inlines = (AccountInline,)
# Register your models here.
class randomStringAdmin(admin.ModelAdmin):
    list_display = ('user','random')

admin.site.unregister(User)
admin.site.register(User,CustomizeUserAdmin)
admin.site.register(randomString,randomStringAdmin)
admin.site.register(VerifyUser)

