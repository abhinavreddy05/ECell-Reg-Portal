# Generated by Django 4.2.2 on 2023-07-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empresario", "0009_empresarioquestionnaire_miscellaneous_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="empresarioquestionnaire",
            name="reach",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
