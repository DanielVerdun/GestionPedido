

# Creacion de class carro.py
# Se crea la funcionalidad de carro para luego poder aplicarla sobre la imagen de
# un carrito de compra Web

class Carro():
    def __init__(self,request): # Metodo constructor/ inicializando el carro
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")

        if not carro:
            carro = self.session["carro"] = {}
        #else:
        self.carro = carro

# Funcion para agregar productos
    """
        Esta funcion agrega productos al carro controlando si el producto
        existe o no. Si el producto no existe lo agrega y en caso de ya
        existir dentro, le incrementa uno a la cantidad .
    """
    def agregar(self,producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for key,value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]+1
                    break
            self.guardar_carro() #llamado a la funcion de guardar_carro()

    #Guarda la session del carro y su contenido
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    #Elimina un producto del carro y guarda la session
    def eliminar(self,producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro() # llamado a la funcion guardar_carro()

    #Resta un producto al carro,resta una unidad
    def restar(self,producto):
        for key,value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar() # llamado a la funcion eliminar()
                    break
        self.guardar_carro() #llamado a la funcion de guardar_carro()

    #Limpia el carro y lo deja basio como desde el comienzo
    def limpiar(self):
        self.session["carro"] = {}
        self.session.modified = True








