from django.contrib import admin
from . import views
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm

urlpatterns = [
    path('', views.register, name="lsm_home"),
    path('register/', views.register, name="lsm_register"),
    path('login/',  LoginView.as_view(template_name='lsm/login.html', authentication_form=CustomAuthenticationForm), name="lsm_login"),

    path('dashboard/', views.dashboard, name="lsm_dashboard"),

    path('logout/', LogoutView.as_view(template_name='lsm/mainpage.html'), name='logout'),
]