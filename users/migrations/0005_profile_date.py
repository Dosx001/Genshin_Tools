# Generated by Django 3.1.2 on 2020-12-03 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
