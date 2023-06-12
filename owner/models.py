from django.db import models


# Create your models here.

class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=25)
    edad = models.IntegerField(default=0)
    dni = models.CharField(max_length=8, default='00000000')
    vigente = models.BooleanField(default=True)
    descripcion = models.TextField(max_length=1000)
