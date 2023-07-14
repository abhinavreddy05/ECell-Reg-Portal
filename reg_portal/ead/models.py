from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from datetime import date
import random
class EADUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=15, unique=True)
    college_name = models.CharField(max_length=255)
    CITY_CHOICES = [
        ('hyderabad', 'Hyderabad'),
        ('chennai', 'Chennai'),
        ('kochi', 'Kochi'),
        # Add more choices as needed
    ]
    ead_city = models.CharField(max_length=255, choices=CITY_CHOICES)
    is_ca = models.BooleanField('campus ambassador', default=False)
    profile_image = models.ImageField(null=True, blank=True, upload_to='ead/profiles/')
    referral_code = models.CharField(max_length=6, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if self.is_ca and not self.referral_code:
            self.referral_code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        code = self.generate_random_code()
        while EADUser.objects.filter(referral_code=code).exists():
            code = self.generate_random_code()
        return code

    def generate_random_code(self):
        # Generate a random 6-digit number
        return str(random.randint(100000, 999999))
    
class EADNotice(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    date = models.DateField(default=date.today, blank=True)

    def __str__(self):
        return self.title