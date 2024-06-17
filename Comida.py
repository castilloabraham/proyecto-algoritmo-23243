from Producto import Producto

class Comida(Producto):
    
    #constructor
    def __init__(self, nombre, cantidad, precio, stock, tipo, vendidos, empaquetado):
        super().__init__(nombre, cantidad, precio, stock, tipo, vendidos)
        self.empaquetado = empaquetado
    
    #Metodos
    
    #metodo mostrar 
    def mostrar(self):
        print(f"nombre: {self.nombre} cantidad: {self.cantidad} precio: {self.precio} stock: {self.stock} tipo: {self.tipo} vendidos: {self.vendidos} empaquetado: {self.empaquetado}")