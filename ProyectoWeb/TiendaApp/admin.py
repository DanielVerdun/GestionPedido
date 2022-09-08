from django.contrib import admin
from .models import CategoriaProd,Productos# importamos los modelos que vamos a trabajar desde el admin

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")#declaro los campos de solo lectura


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")#declaro los campos de solo lectura

admin.site.register(CategoriaProd,CategoriaProdAdmin)
admin.site.register(Productos,ProductoAdmin)


