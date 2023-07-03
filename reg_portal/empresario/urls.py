from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import CustomAuthenticationForm

urlpatterns = [
    path('', views.register, name="empresario_home"),
    path('register/', views.register, name="empresario_register"),
    path('login/',  LoginView.as_view(template_name='empresario/login.html', authentication_form=CustomAuthenticationForm), name="empresario_login"),

    path('dashboard/', views.dashboard, name="empresario_dashboard"),

    path('logout/', LogoutView.as_view(template_name='customUser/mainpage.html'), name='logout'),
]