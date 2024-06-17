
class Cliente():
    
    #constructor
    def __init__(self, nombre, cedula, edad, vip, wallet, entradas_compradas):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.vip = vip
        self.wallet = wallet
        self.entradas_compradas = entradas_compradas
    
    #Metodos
    
    #metodo mostrar 
    def mostrar(self):
        print(f" nombre: {self.nombre} cedula: {self.cedula} edad: {self.edad} vip: {self.vip} wallet: {self.wallet} entradas_compradas: {self.entradas_compradas}")