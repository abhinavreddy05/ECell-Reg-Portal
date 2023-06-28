from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class LSMUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=15, unique=True)
    CITY_CHOICES = [
        ('hyderabad', 'Hyderabad'),
        ('chennai', 'Chennai'),
        ('kochi', 'Kochi'),
        # Add more choices as needed
    ]
    lsm_city = models.CharField(max_length=255, choices=CITY_CHOICES)
    startup = models.BooleanField('have startup', default=False)
    SECTOR = [
        ('agritech', 'Agri Tech'),
        ('fintech', 'Fin Tech'),
        ('other', 'other'),
        # Add more choices as needed
    ]
    sector = models.CharField(max_length=255, choices=SECTOR)

    def __str__(self):
        return self.user.username