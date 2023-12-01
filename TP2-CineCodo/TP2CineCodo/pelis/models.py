from django.db import models

# Create your models here.
class Peli(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Título")
    imagen = models.ImageField(upload_to="pelis", verbose_name="Imagen")
    tipo = models.CharField(max_length=100, verbose_name="Tipo", default="PROXIMAMENTE")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.nombre

#class Proxima(models.Model):
#    nombre = models.CharField(max_length=200, verbose_name="Título")
#    imagen = models.ImageField(upload_to="pelis", verbose_name="Imagen")
#    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

#    def __str__(self):
#        return self.nombre


#class Estreno(models.Model):
#    nombre = models.CharField(max_length=200, verbose_name="Título")
#    imagen = models.ImageField(upload_to="pelis", verbose_name="Imagen")
#    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

#    def __str__(self):
#        return self.nombre
    