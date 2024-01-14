from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to="users_imgs/")

    def __str__(self):
        return self.user.username
