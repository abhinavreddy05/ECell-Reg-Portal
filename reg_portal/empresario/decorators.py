from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def empresario(user):
    return user.is_authenticated and user.empresario

def for_empresario(view_func):
    decorated_view_func = user_passes_test(empresario, login_url='empresario_register')
    return decorated_view_func(view_func)