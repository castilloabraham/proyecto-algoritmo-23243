class Equipo():
    
    #constructor
    def __init__(self, id, Nombre_pais, codigo_fifa, grupo):
        self.id = id
        self.Nombre_pais = Nombre_pais
        self.codigo_fifa = codigo_fifa
        self.grupo = grupo
    
    #Metodos
    
    #metodo mostrar 
    def mostrar(self):
        print(f"id: {self.id} Nombre_pais: {self.Nombre_pais} codigo_fifa: {self.codigo_fifa} grupo: {self.grupo}")