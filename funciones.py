from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Cliente import Cliente
from Boleto import Boleto
from Producto import Producto
from Comida import Comida
from Bebida import Bebida

def carga_API():
    pass

#opcion 1 del menu
def Busqueda_partidos():
    opciones = ["Buscar todos los partidos de un pais", "Buscar todos los partidos que se jugaran en un estadio especifico", "Buscar todos los partidos que se jugaran en una fecha determinada"]
    opcion = menu(opciones)

    if opcion == 0:
        print("Buscar todos los partidos de un pais")
    elif opcion == 1:
        print("Buscar todos los partidos que se jugaran en un estadio especifico")
    elif opcion == 2:
        print("Buscar todos los partidos que se jugaran en una fecha determinada")

#opcion 2 del menu    
def Comprar_entradas():
    pass
#opcion 3 del menu
def Entrar_partido():
    pass
#opcion 4 del menu
def restaurantes():
    pass
#opcion 5 del menu
def Indicadores():
    opciones = ["¿Cuál es el promedio de gasto de un cliente VIP en un partido (ticket + restaurante)?", "Mostrar tabla con la asistencia a los partidos de mejor a peor", 
                "¿Cuál fue el partido con mayor asistencia?", "¿Cuál fue el partido con mayor boletos vendidos?", "Top 3 productos más vendidos en el restaurante.",
                "Top 3 de clientes (clientes que más compraron boletos)", "Salir"]
    
    opcion = menu(opciones)

    if opcion == 0:
        print("¿Cuál es el promedio de gasto de un cliente VIP en un partido (ticket + restaurante)?")
    elif opcion == 1:
        print("Mostrar tabla con la asistencia a los partidos de mejor a peor")
    elif opcion == 2:
        print("¿Cuál fue el partido con mayor asistencia?")
    elif opcion == 3:
        print("¿Cuál fue el partido con mayor boletos vendidos?")
    elif opcion == 4:
        print("Top 3 productos más vendidos en el restaurante.")
    elif opcion == 5:
        print("Top 3 de clientes (clientes que más compraron boletos)")
    else:
        pass

#menu - despliegue de opciones de una lista y validacion de 
def menu(opciones):
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")
    
    opcion = input("ingrese el numero de la opcion que desea elegir: ")
    while not opcion.isnumeric() or not int(opcion) in range(1, len(opciones)+1):
        opcion = input("Error, ingrese el numero de la opcion que desea elegir: ")

    opcion = int(opcion)-1

    return opcion
