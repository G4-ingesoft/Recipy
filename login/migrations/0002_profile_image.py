# Generated by Django 4.2.7 on 2023-11-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/user_defect.png', upload_to=''),
        ),
    ]
