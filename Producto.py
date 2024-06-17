
class Producto():
    
    #constructor
    def __init__(self, nombre, cantidad, precio, stock, tipo, vendidos):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.stock = stock
        self.tipo = tipo
        self.vendidos = vendidos
    
    #Metodos
    
    #metodo mostrar 
    def mostrar(self):
        print(f"nombre: {self.nombre} cantidad: {self.cantidad} precio: {self.precio} stock: {self.stock} tipo: {self.tipo} vendidos: {self.vendidos}")