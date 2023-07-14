from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EADUser, EADNotice

class EADUserAdmin(admin.ModelAdmin):
    pass

class EADNoticeAdmin(admin.ModelAdmin):
    pass

admin.site.register(EADUser, EADUserAdmin)
admin.site.register(EADNotice, EADNoticeAdmin)