
class Boleto():
    
    #constructor
    def __init__(self, id, tipo_clase, precio, partido, asiento):
        self.id = id
        self.tipo_clase = tipo_clase
        self.precio = precio
        self.partido = partido
        self.asiento = asiento
    
    #Metodos
    
    #metodo mostrar 
    def mostrar(self):
        print(f" id: {self.id} tipo_clase: {self.tipo_clase} precio: {self.precio} partido: {self.partido} asiento: {self.asiento}")