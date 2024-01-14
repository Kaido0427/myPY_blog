from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    titre = models.CharField(max_length=50)
    contenu = models.TextField()
    image = models.FileField(upload_to="posts_imgs/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    contenu = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenu


class Reaction(models.Model):
    reaction_Type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.reaction_Type
