class Partido():
    
    #constructor
    def __init__(self, id, numero, equipo_local, equipo_visitante, fecha_hora, estadio, asistencia, ventas):
        self.id = id
        self.numero = numero
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha_hora = fecha_hora
        self.estadio = estadio
        self.asistencia = asistencia
        self.ventas = ventas
    
    #Metodos
    
    #metodo mostrar 
    def mostrar(self):
        print(f"id: {self.id} numero: {self.numero} equipo_local: {self.equipo_local} equipo_visitante: {self.equipo_visitante} fecha y hora: {self.fecha_hora} estadio: {self.estadio} asistencia: {self.asistencia} ventas: {self.ventas}")