from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

from profiles.models import Profile

# Create your models here.
class Receta(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receta')
    name = models.CharField(default="no name", max_length=100)
    image = models.ImageField(default='images/Receta_defect.png')
    timestamp = models.DateTimeField(default=timezone.now)
    content= models.TextField()
    

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.user.username}:{self.content}'