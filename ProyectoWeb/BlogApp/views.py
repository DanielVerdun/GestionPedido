from django.shortcuts import render
from BlogApp.models import Post,Categoria
# Create your views here.

def blog(request):
     # Todos los objetos  de la class Post y lo guardamos dentro de la variable.
    posts = Post.objects.all()

    return render(request, "blog/blog.html",{"posts":posts})

def categoria(request,categoria_id):
     #filtra los post de la categoria que reciba  en el parametro categoria_id
     categoria=Categoria.objects.get(id=categoria_id)
     posts = Post.objects.filter(categorias=categoria)

     return render(request,"blog/categoria.html",{"categoria":categoria, "posts":posts})
    