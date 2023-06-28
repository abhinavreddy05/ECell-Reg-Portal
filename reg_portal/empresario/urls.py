from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.register, name="empresario_home"),
    path('register/', views.register, name="empresario_register"),
    path('login/',  LoginView.as_view(template_name='empresario/login.html'), name="empresario_login"),

]