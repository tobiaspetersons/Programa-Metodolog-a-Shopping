from usuarios import iniciar_sesion, registrar_cliente
from variables_globales import USUARIOS
from administrador import agregar_admin
from utils import clear_screen, verificar_vencimiento_promos

def main():
    clear_screen()
    verificar_vencimiento_promos()
    if not any(usuario['rol'] == 'admin' for usuario in USUARIOS):
        agregar_admin(lista=USUARIOS)
    while True:
        print("----------------------------------------------")
        print("Menú Principal:")
        print("1. Ingresar con email registrado")
        print("2. Registrarse como cliente")
        print("3. Salir")
        print("----------------------------------------------")
        opcion = input("Seleccione una opción (1/2/3): ")
        if opcion == "1":
            clear_screen()
            iniciar_sesion()
        elif opcion == "2":
            clear_screen()
            registrar_cliente()
        elif opcion == "3":
            clear_screen()
            print("¡Hasta luego!")
            break
        else:
            clear_screen()
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
        
if __name__ == "__main__":
    main() 
