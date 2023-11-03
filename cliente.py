from promociones import usar_promociones_cliente, ver_locales
from utils import clear_screen

def menu_cliente(usuario_encontrado:list):
    clear_screen()
    while True:
        print("1. Buscar descuentos en local")
        print("2. Ver locales disponibles")
        print("0. Salir")
        opcion= input("Seleccione una opcion (1/0): ")
        if opcion== "1":
            usar_promociones_cliente(usuario_encontrado=usuario_encontrado)
        elif opcion == "2":
            ver_locales()
        elif opcion == "0":
            clear_screen()
            print("¡Hasta luego!")
            break
        else:
            clear_screen()
            print("Opción no válida. Por favor, seleccione 1 o 0.")
            