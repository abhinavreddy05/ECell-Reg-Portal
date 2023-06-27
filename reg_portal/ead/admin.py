from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EADUser

class EADUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(EADUser, EADUserAdmin)