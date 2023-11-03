from usuarios import iniciar_sesion, registrar
from variables_globales import USUARIOS
from utils import clear_screen, verificar_vencimiento_promos

def main():
    clear_screen()
    verificar_vencimiento_promos()
    if not any(usuario['rol'] == 'admin' for usuario in USUARIOS):
        registrar(rol='admin',mensaje_nombre="ADMINISTRADOR, Ingrese su nombre: ")
    while True:
        print("----------------------------------------------")
        print("Menú Principal:")
        print("1. Ingresar con email registrado")
        print("2. Registrarse como cliente")
        print("0. Salir")
        print("----------------------------------------------")
        opcion = input("Seleccione una opción (1/2/0): ")
        if opcion == "1":
            clear_screen()
            iniciar_sesion()
        elif opcion == "2":
            clear_screen()
            registrar()
        elif opcion == "0":
            clear_screen()
            print("¡Hasta luego!")
            break
        else:
            clear_screen()
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
        
if __name__ == "__main__":
    main() 
