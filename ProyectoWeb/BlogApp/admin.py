from django.contrib import admin
from .models import Categoria,Post # importamos los modelos que vamos a trabajar desde el admin

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("create","update")


class PostAdmin(admin.ModelAdmin):
    readonly_fields=("create","update")

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostAdmin)