from Producto import Producto

class Bebida(Producto):
    
    #constructor
    def __init__(self, nombre, cantidad, precio, stock, tipo, vendidos, tiene_alcohol):
        super().__init__(nombre, cantidad, precio, stock, tipo, vendidos)
        self.tiene_alcohol = tiene_alcohol
    
    #Metodos
    
    #metodo mostrar 
    def mostrar(self):
        print(f"nombre: {self.nombre} cantidad: {self.cantidad} precio: {self.precio} stock: {self.stock} tipo: {self.tipo} vendidos: {self.vendidos} tiene_alcohol: {self.tiene_alcohol}")