
from django.urls import path
from  . import views

app_name= "carro"# nombre declarativo para utilizar las funciones de forma ordenada.
# en cuanto se quiera llamar a las funciones poniendo el app_name delante de la funcion
# evitamos colición en caso de haber otra funcion con el mismo nombre.

urlpatterns = [
    #Declaramos las urls del carro
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),


]