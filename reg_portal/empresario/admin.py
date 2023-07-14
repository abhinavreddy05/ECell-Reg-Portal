from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EmpresarioUser, EmpresarioQuestionnaire, EmpresarioNotice

class EmpresarioUserAdmin(admin.ModelAdmin):
    pass

class EmpresarioQuestionnaireAdmin(admin.ModelAdmin):
    pass

class EmpresarioNoticeAdmin(admin.ModelAdmin):
    pass

admin.site.register(EmpresarioUser, EmpresarioUserAdmin)
admin.site.register(EmpresarioQuestionnaire, EmpresarioQuestionnaireAdmin)
admin.site.register(EmpresarioNotice, EmpresarioNoticeAdmin)