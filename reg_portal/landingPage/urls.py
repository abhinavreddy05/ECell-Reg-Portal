from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
]