from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class EmpresarioUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    company_startup_name = models.CharField(max_length=255)
    team_leader = models.CharField(max_length=255)
    team_leader_linkedin = models.URLField(max_length=255)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('transgender', 'Transgender'),
        ('other', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    age = models.IntegerField()
    location= models.CharField(max_length=255)
    primary_email = models.EmailField()
    primary_contact = models.CharField(max_length=15, unique=True)
    cofounder = models.CharField(max_length=255, null=True)
    cofounder_email = models.EmailField(null=True)
    cofounder_contact = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username