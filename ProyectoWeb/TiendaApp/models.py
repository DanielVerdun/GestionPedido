
from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True) #registra la fecha de creacion de forma automatica
    updated = models.DateTimeField(auto_now_add=True) #registra la fecha de actualizacion

    class Meta():
        verbose_name = "categoriaprod"
        verbose_name_plural = "categoriasprod"

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProd,on_delete=models.CASCADE)#clave foranea
    imagen = models.ImageField(upload_to= 'tienda',null=True, blank=True)# campo imagen
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)#por default esta disponible.
    created = models.DateTimeField(auto_now_add=True) #registra la fecha de creacion de forma automatica
    updated = models.DateTimeField(auto_now_add=True) #registra la fecha de actualizacion


    class Meta():
        verbose_name="producto"
        verbose_name_plural = "productos"

        def __str__(self):
            return self.nombre

