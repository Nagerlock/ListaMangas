from django.db import models


class manga(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField(blank=True)


class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200)