from django.db import models

# Create your models here.

class Servicios(models.Model):
    
    titulo = models.CharField(max_length= 50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'sevicos') #carpeta donde se guardaran los archivos media dentro de esta app
    create = models.DateField(auto_now_add=True) #fecha automatica
    update = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
       return self.titulo
