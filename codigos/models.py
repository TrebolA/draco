from django.db import models
from django.utils import timezone

class Codigo(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    apellido = models.CharField(max_length=200, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    terminos = models.BooleanField(default=False)
    politica = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
