# Generated by Django 4.2.7 on 2023-11-15 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_profile_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]