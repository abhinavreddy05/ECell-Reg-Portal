from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from datetime import date

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
    age = models.IntegerField(null=True)
    location= models.CharField(max_length=255)
    primary_email = models.EmailField()
    primary_contact = models.CharField(max_length=15, unique=True)
    cofounder = models.CharField(max_length=255, blank=True, null=True)
    cofounder_email = models.EmailField(blank=True, null=True)
    cofounder_contact = models.CharField(blank=True, null=True, max_length=15)
    questionare_submitted = models.BooleanField(default=False)
    profile_image = models.ImageField(null=True, blank=True, upload_to='empresario/profiles/')
    
    def __str__(self):
        return self.user.username


class EmpresarioQuestionnaire(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    SECTOR = [
        ('agritech', 'Agri Tech'),
        ('fintech', 'Fin Tech'),
        ('other', 'other'),
        # Add more choices as needed
    ]
    sector = models.CharField(max_length=255, choices=SECTOR)
    STAGE = [
        ('ideation', 'Ideation'),
        ('preseed', 'Pre-seed'),
        ('seed', 'Seed'),
        ('earlystage', 'Early Stage'),
        ('seriesAandbeyond', 'Series A & beyond'),
        # Add more choices as needed
    ]
    stage = models.CharField(max_length=255, choices=STAGE)
    problem_solving= models.CharField(max_length=255)
    proposed_solution= models.CharField(max_length=255)
    MONEY_RAISED = [
        ('<50k', '< 50K'),
        ('50k_1l', '50K - 1L'),
        ('1l_3l', '1L - 3L'),
        ('3l-7.5l', '3L - 7.5L'),
        ('7.5l_20l', '7.5L - 20L'),
        ('>20l', '20L & more'),
    ]
    money_raised = models.CharField(max_length=255, choices=MONEY_RAISED)
    IPSTAGE = [
        ('not_applicable', 'Not applicable in my case'),
        ('patent_pending', 'Patent pending'),
        ('secured_patents', 'Secured patents'),
        ('haventfilled', "Haven't filled the patent but has the potential to create IP portfolio"),
    ]
    ip_stage = models.CharField(max_length=255, choices=IPSTAGE)
    website_link = models.URLField(max_length=255, null=True, blank=True)
    miscellaneous = models.CharField(max_length=255, null=True, blank=True)
    pitch_deck = models.FileField(null=True, blank=True, upload_to='empresario/pitchdeck/')
    supporting_docs = models.CharField(max_length=255)
    miscellaneous = models.CharField(max_length=255)
    reach = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.user.username


class EmpresarioNotice(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    date = models.DateField(default=date.today, blank=True)

    def __str__(self):
        return self.title

