"""
    Creo archivo context_procesor.py para crear una variable global donde se almacenara
    el total de la compra. A su ves estaŕa disponible desde todo el proyecto.
"""
#Creo un metodo que me crea la variable global

def importe_total_carro(request):
    total = 0 # inicializo la variable en 0 para proximamente almacenar el total de la compra
    # verifico si el usuario esta autenticado
    if request.user.is_authenticated:
    #Recorro las clave valor que estan dentro del carro.
        for key, value in request.session["carro"].items():
            total = total+(float(value["precio"])*value["cantidad"])#multiplico el valor precio por el valor cantidad

    return {"importe_total_carro":total}

"""def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:

        if 'carro' in request.session.keys():
            for key,value in request.session['carro'].items():
                total = total +(float(value['precio'])*value['cantidad'])
                #total+= int(value['cantidad'])
        return {'importe_total_carro':total}"""
