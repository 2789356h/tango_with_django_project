# Generated by Django 2.2.28 on 2024-02-29 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0010_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
