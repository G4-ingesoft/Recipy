# Generated by Django 4.2.7 on 2023-11-15 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_user_receta_user_receta_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='name',
            field=models.TextField(default='no name', max_length=100),
        ),
    ]
