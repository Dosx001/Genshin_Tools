# Generated by Django 3.1.2 on 2020-12-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_blessing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blessing',
            field=models.BooleanField(default=False),
        ),
    ]
