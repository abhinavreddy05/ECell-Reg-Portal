from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EmpresarioUser

class EmpresarioUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(EmpresarioUser, EmpresarioUserAdmin)