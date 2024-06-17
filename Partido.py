class Partido():
    
    #constructor
    def __init__(self, equipo_local, equipo_visitante, fecha, hora, estadio, asistencia, ventas):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.hora = hora
        self.estadio = estadio
        self.asistencia = asistencia
        self.ventas = ventas
    
    #Metodos
    
    #metodo mostrar 
    def mostrar(self):
        print(f" equipo_local: {self.equipo_local} equipo_visitante: {self.equipo_visitante} fecha: {self.fecha} hora: {self.hora} estadio: {self.estadio} asistencia: {self.asistencia} ventas: {self.ventas}")