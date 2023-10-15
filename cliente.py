from promociones import usar_promociones_cliente
from utils import clear_screen
def menu_cliente():
    while True:
        clear_screen()
        print("1. Buscar descuentos en local")
        print("2. Solicitar descuento")
        print("0. Salir")
        opcion_cliente = input("Seleccione una opcion (1/2/0): ")
        if opcion_cliente == "1":
            usar_promociones_cliente()
        elif opcion_cliente == "0":
            clear_screen()
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1 o 0.")