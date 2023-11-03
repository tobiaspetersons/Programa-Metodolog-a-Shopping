from locales import menu_gestion_locales
from promociones import solicitudes_promociones_admin
from listados import listado_locales,listado_promociones_usadas,listado_usuarios
from utils import clear_screen

def menu_administrador():
    clear_screen()
    while True:
        print("----------------------------------------------")
        print("1. Gestion de locales")
        print("2. Aprobar / Denegar solicitud de descuento")
        print("3. Listado de utilización de descuentos")
        print("4. Listado de locales")
        print("5. Listado de usuarios")
        print("0. Salir")
        print("----------------------------------------------")
        opcion_admin = input("Seleccione una opción (1/2/3/0): ")
        if opcion_admin == "1":
            menu_gestion_locales()
        elif opcion_admin == "2":
            solicitudes_promociones_admin()
        elif opcion_admin == "3":
            listado_promociones_usadas()
        elif opcion_admin == "4":
            listado_locales()
        elif opcion_admin == "5":
            listado_usuarios()
        elif opcion_admin == "0":
            clear_screen()
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 0,1,2 o 3.")
                

