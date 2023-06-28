from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)

    ead = models.BooleanField('registered for ead', blank=True, default=False)
    lsm = models.BooleanField('registered for lsm', blank=True, default=False)
    empresario = models.BooleanField('registered for empresario', blank=True, default=False)
    
    # Add related_name argument to avoid clash with auth.User.groups
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    
    # Add related_name argument to avoid clash with auth.User.user_permissions
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')

