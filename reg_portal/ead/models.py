from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class EADUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=15)
    college_name = models.CharField(max_length=255)
    CITY_CHOICES = [
        ('hyderabad', 'Hyderabad'),
        ('chennai', 'Chennai'),
        ('kochi', 'Kochi'),
        # Add more choices as needed
    ]
    ead_city = models.CharField(max_length=255, choices=CITY_CHOICES)

    def __str__(self):
        return self.user.username