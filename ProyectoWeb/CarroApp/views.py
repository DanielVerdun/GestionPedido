from django.shortcuts import render
from .carro import Carro # importacion de la class Carro para disponer de la funcionalidad de carro.py
#importacion del modelo Productos que se encuentra en la TiendaApp.models
from TiendaApp.models import Productos
from django.shortcuts import redirect

# Create your views here.

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