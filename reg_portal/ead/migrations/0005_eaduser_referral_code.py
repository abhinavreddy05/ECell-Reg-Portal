# Generated by Django 4.2.2 on 2023-07-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ead", "0004_eadnotice_eaduser_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="eaduser",
            name="referral_code",
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]
