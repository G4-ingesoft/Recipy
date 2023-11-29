from django.db import models

from profiles.models import Profile
from post.models import Receta
from django.utils import timezone

# Create your models here.
class Comentario(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    text = models.CharField(max_length=255,default="no comment")
    creacion = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-creacion']

    def __str__(self):
        return f'comentario de {self.user.user.username} en la receta {self.receta.name}'