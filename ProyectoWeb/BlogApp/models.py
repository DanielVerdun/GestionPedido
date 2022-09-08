from django.db import models
from django.contrib.auth.models import User #importamos la clase User

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(max_length= 50)
    create = models.DateField(auto_now_add=True) #fecha automatica
    update = models.DateField(auto_now_add=True) #actualizacion de fecha

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
       return self.nombre #convierte en string lo que queremos ver

class Post(models.Model):

    titulo = models.CharField(max_length= 50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'blog',null=True,blank=True) #carpeta donde se guardaran los archivos media dentro de esta app. con null/blank indicamos que la imagen puede ser opcional
    autor = models.ForeignKey(User,on_delete=models.CASCADE)#borra todo los post cuando se borra el user
    categorias = models.ManyToManyField(Categoria)
    create = models.DateField(auto_now_add=True) #fecha automatica
    update = models.DateField(auto_now_add=True) #actualizacion automatica

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
       return self.titulo       