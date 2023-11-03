from promociones import gestion_promociones
from utils import clear_screen
from listados import listado_promociones_local

def menu_duenio(usuario_encontrado:list):
    clear_screen()
    while True:
        print("----------------------------------------------")
        print("1. Gestion de descuentos")
        print("2. Reporte de uso de descuentos")
        print("0. Salir")
        print("----------------------------------------------")
        opcion_dueño = input("Seleccione una opcion (1/2/3/0): ")
        if opcion_dueño == "1":
            gestion_promociones(usuario_encontrado=usuario_encontrado)
        elif opcion_dueño == "2":
            listado_promociones_local(usuario_encontrado=usuario_encontrado)
        elif opcion_dueño == "0":
            clear_screen()
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2, o 0.")