from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone
from datetime import timedelta

from profiles.models import Profile
from utilities.imgur_api import upload_image_imgur
from PIL import Image

from django.urls import reverse

# Create your models here.
class Receta(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receta')
    name = models.CharField(default="no name", max_length=100)
    image = models.ImageField(default='images/Receta_defect.png')
    imgurl = models.CharField(default="no url",max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    prep_time = models.DurationField(default=timedelta(hours=0, minutes=00)) # Tiempo de preparación, tipo 1:00:30
    description = models.TextField(default="Sin descripción.")
    ingredients = models.TextField(default="Sin ingredientes.")
    steps = models.TextField(default="Sin pasos de preparación.")
    # comentarios = models.IntegerField(default=0)

    class Meta:
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Antes de guardar, convierte la imagen y almacénala en el campo image
        print("Receta save, img = "+str(self.image))
        ###SOLUCIÓN TEMPORAL, LO IDEAL ES TENER SAVES DIFERENTES PARA UPDATE Y PARA CREATE, ASI SE EVITA ESTO
        if self.image.name != "images/Receta_defect.png":
            img = Image.open(self.image.path)
            if img.height > 1440 or img.width > 1440:
                img.thumbnail((1440,1440))
                img.save(self.image.path)
            ##Decidir si subir la tumbnail supongo aqui se sube la thumbnail
            self.imgurl = upload_image_imgur(self.image.path)
            ##Es necesario subirlo dos veces
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.user.username}:{self.content}'
    
    def get_absolute_url(self):
        return reverse("receta_detail", kwargs={"pk": self.pk})
    
'''    
class Comentario(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='comentarios')
    receta = models.ForeignKey(Receta,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.user.username}:{self.content}'
'''
