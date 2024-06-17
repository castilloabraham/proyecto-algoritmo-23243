class Estadio():
    
    #constructor
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
    
    #Metodos
    
    #metodo mostrar 
    def mostrar(self):
        print(f"nombre: {self.nombre} ubicacion: {self.ubicacion}")