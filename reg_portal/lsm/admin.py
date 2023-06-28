from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LSMUser

class LSMUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(LSMUser, LSMUserAdmin)