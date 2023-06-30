# Generated by Django 4.1.7 on 2023-06-29 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0003_customuser_empresario'),
        ('empresario', '0002_alter_empresariouser_cofounder_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresarioQuestionnaire',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sector', models.CharField(choices=[('agritech', 'Agri Tech'), ('fintech', 'Fin Tech'), ('other', 'other')], max_length=255)),
                ('stage', models.CharField(choices=[('ideation', 'Ideation'), ('preseed', 'Pre-seed'), ('seed', 'Seed'), ('earlystage', 'Early Stage'), ('seriesAandbeyond', 'Series A & beyond')], max_length=255)),
                ('problem_solving', models.CharField(max_length=255)),
                ('proposed_solution', models.CharField(max_length=255)),
                ('money_raised', models.CharField(choices=[('<50k', '< 50K'), ('50k_1l', '50K - 1L'), ('1l_3l', '1L - 3L'), ('3l-7.5l', '3L - 7.5L'), ('7.5l_20l', '7.5L - 20L'), ('>20l', '20L & more')], max_length=255)),
                ('ip_stage', models.CharField(choices=[('not_applicable', 'Not applicable in my case'), ('patent_pending', 'Patent pending'), ('secured_patents', 'Secured patents'), ('haventfilled', "Haven't filled the patent but has the potential to create IP portfolio")], max_length=255)),
                ('website_link', models.URLField(max_length=255, null=True)),
            ],
        ),
    ]