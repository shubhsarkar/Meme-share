from django.db import models

# Create your models here.
class Meme(models.Model):

    owner = models.CharField(max_length=100, default="")
    url = models.URLField(default="")
    cap = models.TextField(max_length=200, default="")
    