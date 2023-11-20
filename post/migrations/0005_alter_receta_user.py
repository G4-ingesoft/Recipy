# Generated by Django 4.2.7 on 2023-11-20 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_description'),
        ('post', '0004_alter_receta_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receta', to='profiles.profile'),
        ),
    ]
