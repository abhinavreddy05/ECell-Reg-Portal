from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def lsm(user):
    return user.is_authenticated and user.lsm

def for_lsm(view_func):
    decorated_view_func = user_passes_test(lsm, login_url='lsm_register')
    return decorated_view_func(view_func)