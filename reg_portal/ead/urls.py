from django.contrib import admin
from . import views
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm

urlpatterns = [
    path('', views.register, name="ead_home"),
    path('register/', views.register, name="ead_register"),
    path('login/',  LoginView.as_view(template_name='ead/login.html', authentication_form=CustomAuthenticationForm), name="ead_login"),

    path('dashboard/', views.dashboard, name="ead_dashboard"),
    path('result/', views.result, name="ead_result"),
    path('event/', views.event, name="ead_event"),
    path('certificate/', views.certificate, name="ead_certificate"),

    path('logout/', LogoutView.as_view(template_name='customUser/mainpage.html'), name='logout'),
]