from django.shortcuts import render
from ServiciosApp.models import Servicios #importamos la class Servicios de ServiciosApp.models


# Create your views here.

def servicios(request):

    # Todos los objetos  de la class Servicios y lo guardamos dentro de la variable.
    servicios = Servicios.objects.all()

    # Crea el html con los datos que estan en la variable servicios.
    return render(request, "servicios/servicios.html", {"servicios": servicios})