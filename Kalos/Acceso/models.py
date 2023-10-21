from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Clase 24
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.deletion.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{settings.MEDIA_URL}{self.imagen}"