
from funciones import Busqueda_partidos, Comprar_entradas, Entrar_partido, restaurantes, Indicadores, menu, carga_API


def main():
    equipos = []
    estadios = []
    restaurates = []
    productos = []
    partidos = []
    carga_API(equipos, estadios, restaurates, productos, partidos)
    print("Bienvenid@ a la Euro 2024")
    
    while True:
        opciones = ["Busqueda de partidos", "Comprar entradas", "Entrar al partido", "restaurantes", "Indicadores de gestion", "salir"]
        
        opcion = menu(opciones)
        
        if opcion == 0:
            Busqueda_partidos()
        elif opcion == 1:
            Comprar_entradas()
        elif opcion == 2:
            Entrar_partido()
        elif opcion == 3:
            restaurantes()
        elif opcion == 4:
            Indicadores()
        elif opcion == 5:
            print("Hasta luego")
            break

main()