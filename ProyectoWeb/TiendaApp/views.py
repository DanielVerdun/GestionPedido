from django.shortcuts import render, redirect

from .models import Productos
from .carro import Carro

# Create your views here.

def tienda(request):
    productos = Productos.objects.all()#traigo todos los productos

    return render(request,"tienda/tienda.html", {"productos" : productos})

#----Funcionalidades del Carro------

def agregar_producto(request,producto_id):
    carro = Carro(request) #Creamos el carro
    producto = Productos.objects.get(id = producto_id)#obtengo el id del producto que vamos agregar al carro
    carro.agregar(producto = producto)

    return redirect("tienda")

def eliminar_producto(request,producto_id):
    carro = Carro(request) #Creamos el carro
    producto = Productos.objects.get(id = producto_id)#obtengo el id del producto que vamos a eliminar del carro
    carro.eliminar(producto = producto)

    return redirect("tienda")

def restar_producto(request,producto_id):
    carro = Carro(request) #Creamos el carro
    producto = Productos.objects.get(id = producto_id)#obtengo el id del producto que vamos restar al carro
    carro.restar(producto = producto)

    return redirect("tienda")

def limpiar_carro(request):
    carro = Carro(request) #Creamos el carro
    carro.limpiar()

    return redirect("tienda")