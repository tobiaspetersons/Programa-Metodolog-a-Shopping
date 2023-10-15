from manejo_archivos import guardar_archivo
from locales import menu_gestion_locales
from promociones import solicitudes_promociones_admin, reporte_promociones_usadas
from utils import clear_screen
from variables_globales import NOMBRE_ARCHIVO_USUARIOS

NOMBRE_ARCHIVO_USUARIOS = 'usuarios.json'

def agregar_admin(lista:list):
    admin = {
        'cod': 1,
        'email': "a",
        'clave': "a",
        'rol': "admin"
    }
    lista.append(admin)
    guardar_archivo(NOMBRE_ARCHIVO_USUARIOS, lista)
        
def menu_administrador():
    clear_screen()
    while True:
        print("----------------------------------------------")
        print("1. Gestion de locales")
        print("2. Aprobar / Denegar solicitud de descuento")
        print("3. Reporte de utilización de descuentos")
        print("0. Salir")
        print("----------------------------------------------")
        opcion_admin = input("Seleccione una opción (1/2/3/0): ")
        if opcion_admin == "1":
            menu_gestion_locales()
        elif opcion_admin == "2":
            solicitudes_promociones_admin()
        elif opcion_admin == "3":
            reporte_promociones_usadas()
        elif opcion_admin == "0":
            clear_screen()
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 0,1,2 o 3.")
                

