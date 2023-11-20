from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images/user_defect.jpeg')
    description = models.TextField(default=' ')
    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    


def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile,sender=User)