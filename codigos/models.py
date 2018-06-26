from django.db import models


class Codigo(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    apellido = models.CharField(max_length=200, blank=True, null=True)
    celular = models.BigIntegerField(blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    terminos = models.BooleanField(default=False)
    politica = models.BooleanField(default=False)
    codigo = models.CharField(max_length=50, default='None Code')

    def inscribir(self):
        self.save()

    def __str__(self):
        return self.nombre
