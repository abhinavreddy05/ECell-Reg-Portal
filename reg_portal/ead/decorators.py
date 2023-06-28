from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def ead(user):
    return user.is_authenticated and user.ead

def for_ead(view_func):
    decorated_view_func = user_passes_test(ead, login_url='ead_register')
    return decorated_view_func(view_func)