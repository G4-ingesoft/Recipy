from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone
from datetime import timedelta

from profiles.models import Profile

# Create your models here.
class Receta(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receta')
    name = models.CharField(default="no name", max_length=100)
    image = models.ImageField(default='images/Receta_defect.png')
    timestamp = models.DateTimeField(default=timezone.now)
    prep_time = models.DurationField(default=timedelta(hours=0, minutes=00)) # Tiempo de preparación, tipo 1:00:30
    description = models.TextField(default="Sin descripción.")
    ingredients = models.TextField(default="Sin ingredientes.")
    steps = models.TextField(default="Sin pasos de preparación.")
    

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}:{self.content}'