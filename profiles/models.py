from typing import Any
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from utilities.imgur_api import upload_image_imgur
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.CharField(default="../../static/images/user_defect.jpeg",max_length=255)
    image = models.ImageField(default='default_profile_image.jpeg',upload_to='profile_pics')
    description = models.TextField(default=' ')
    #imgurl = models.CharField(default=default_imgurl,max_length=255)
    imgurl = models.CharField(default="https://i.imgur.com/fKgDDZl.jpeg",max_length=255)

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs)
        # Antes de guardar, convierte la imagen y almacénala en el campo image
        print("Profile save, img = "+str(self.image))
        ###SOLUCIÓN TEMPORAL, LO IDEAL ES TENER SAVES DIFERENTES PARA UPDATE Y PARA CREATE, ASI SE EVITA ESTO
        if self.image.name != "default_profile_image.jpeg":
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                img.thumbnail((300,300))
                img.save(self.image.path)
            ##Decidir si subir la tumbnail supongo aqui se sube la thumbnail
            self.imgurl = upload_image_imgur(self.image.path)
            ##Es necesario subirlo dos veces
            super().save(*args, **kwargs)

    
    
# from django.dispatch import receiver
# @receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile,sender=User)

