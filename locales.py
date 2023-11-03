from utils import buscar_cod_maximo,clear_screen, ingresar_dato, ingresar_dato_modificado, ingresar_num_formato, input_number
from manejo_archivos import guardar_archivo
from variables_globales import NOMBRE_ARCHIVO_USUARIOS, NOMBRE_ARCHIVO_LOCALES, LOCALES, USUARIOS

def menu_gestion_locales():
    clear_screen()
    while True:
        print("-------------------------------------------------------------")
        print("a) Crear Locales")
        print("b) Modificar Local")
        print("c) Eliminar Local")
        print("d) Control de locales activos")
        print("e) Volver")
        print("-------------------------------------------------------------")
        opcion_gestion = input("Seleccione una opción (a/b/c/d/e): ")
        if opcion_gestion == "a":
            crear_local()
        elif opcion_gestion == "b":
            modificar_local()
        elif opcion_gestion == "c":
            eliminar_local()
        elif opcion_gestion == "d":
            lista_locales()
        elif opcion_gestion == "e":
            clear_screen()
            break
        else:
            clear_screen()
            print("Opción no válida. Por favor, seleccione a,b,c,d o e.")
                
def crear_local():
    clear_screen()
    codigo_local = buscar_cod_maximo(LOCALES)
    codigo_duenio = buscar_cod_maximo(USUARIOS)

    while True:
        nombre_nuevo_local = ingresar_dato("Ingrese el nombre del nuevo local (0 para cancelar): ")
        if nombre_nuevo_local == "0":
            clear_screen()
            return
        elif any(local['nombre'] == nombre_nuevo_local for local in LOCALES):
            print('El nombre de local ingresado ya existe.')
        else:
            ubicacion_nuevo_local = ingresar_dato(mensaje='Ingrese la ubicación del nuevo local: ')
            rubro_nuevo_local = ingresar_dato(mensaje='Ingrese el rubro del nuevo local: ')
            nombre_nuevo_duenio = ingresar_dato("Ingrese el nombre del dueño del local: ")
            apellido_nuevo_duenio = ingresar_dato("Ingrese el apellido del dueño del local: ")
            email_nuevo_duenio = f"{nombre_nuevo_local.lower()}@shopping.com"
            clave_nuevo_duenio = f"{nombre_nuevo_local}12345"
            dni_nuevo_duenio = ingresar_num_formato(mensaje='Ingrese el DNI del dueño del local: ',
                                                    cant=8,
                                                    mensaje_error='Formato no válido. Intente nuevamente.'
                                                    )
            telefono_nuevo_duenio = ingresar_num_formato(mensaje='Ingrese el número de teléfono del dueño del local: ',
                                                         cant=10,
                                                         mensaje_error='Formato no válido. Intente nuevamente'
                                                         )           
            nuevo_local = {
                'cod': codigo_local + 1,
                'nombre': nombre_nuevo_local,
                'ubicacion': ubicacion_nuevo_local,
                'rubro': rubro_nuevo_local,
                'estado': True  # activo
            }
            nuevo_dueño = {
                'cod': codigo_duenio + 1,
                'nombre': nombre_nuevo_duenio,
                'apellido': apellido_nuevo_duenio,
                'email': email_nuevo_duenio,
                'clave': clave_nuevo_duenio,
                'rol': 'duenio_local',
                'dni': dni_nuevo_duenio,
                'telefono': telefono_nuevo_duenio
            }
            nuevo_local['cod_usuario'] = nuevo_dueño['cod']
            LOCALES.append(nuevo_local)
            USUARIOS.append(nuevo_dueño)
            guardar_archivo(nombre_archivo=NOMBRE_ARCHIVO_USUARIOS, datos=USUARIOS)
            guardar_archivo(nombre_archivo=NOMBRE_ARCHIVO_LOCALES, datos=LOCALES)
            clear_screen()
            print("\n------------------------------------------------------------------------------------")
            print(f"Local registrado con código {nuevo_local['cod']} y dueño con número de usuario {nuevo_local['cod_usuario']}")
            print("------------------------------------------------------------------------------------")
            break

def modificar_local():
    clear_screen()
    print("Locales disponibles:")
    for local in LOCALES:
        print(f"Código: {local['cod']}, Nombre: {local['nombre']}")
    codigo_local = input_number(message="Ingrese el codigo de local que quiera modificar (0 para cancelar): ",
                                error_message="El valor ingresado no es valido",
                                integer=True
                                )
    while True:
        if codigo_local == 0:
            clear_screen()
            break
        else:
            local_encontrado = []
            for local in LOCALES:
                if local['cod'] == codigo_local:
                    local_encontrado = local
                    break
            print(f"El local seleccionado es {local_encontrado['nombre']}")
            if local_encontrado:
                while True:
                    print('\n--------------------------------------')
                    print("1. Modificar nombre")
                    print("2. Modificar ubicación")
                    print("3. Modificar rubro")
                    print("4. Cambiar estado (Activo/Inactivo)")
                    print ('--------------------------------------')
                    opcion = input_number(message="Seleccione una opción (1/2/3/4): ",
                                error_message="El valor ingresado no es valido. ",
                                integer=True
                                )
                    if opcion == 1:
                        local_encontrado['nombre'] = ingresar_dato_modificado(mensaje=("Ingrese el nuevo nombre del local: "),
                                                                              lista=local_encontrado,
                                                                              key=('nombre'))
                    elif opcion == 2:
                        local_encontrado['ubicacion'] = ingresar_dato_modificado(mensaje=('Ingrese la nueva ubicación del local: '),
                                                                                 lista=local_encontrado,
                                                                                 key=('ubicacion'))
                    elif opcion == 3:
                        local_encontrado['rubro'] = ingresar_dato_modificado(mensaje=("Ingrese el nuevo rubro del local: "),
                                                                             lista=local_encontrado,
                                                                             key=('rubro'))
                    elif opcion == 4:
                        nuevo_estado = not local_encontrado['estado']  
                        local_encontrado['estado'] = nuevo_estado
                        print("Estado cambiado con éxito.")
                    else:
                        print("Opción no valida. Por favor, ingrese 1, 2, 3 o 4")
                    guardar_archivo(nombre_archivo=NOMBRE_ARCHIVO_LOCALES, datos=LOCALES)
                    clear_screen()
                    print("Local modificado con exito.")
    
                    while True:
                        verificacion = input("¿Desea cambiar otro dato del local? (S/N): ").strip().lower()
                        if verificacion == "s":
                            clear_screen()
                            break
                        elif verificacion == "n":
                            return
                        else:
                            print('Ingrese "S" para sí o "N" para no.')
            else:
                print("No se encontró un local con el código ingresado.")
                print("Locales disponibles:")
                for local in LOCALES:
                    print(f"Código: {local['cod']}, Nombre: {local['nombre']}")
                
                
def eliminar_local():
    clear_screen()
    codigo_local = input_number(message="Ingrese el codigo de local que quiera eliminar (0 para cancelar): ",
                                error_message="El valor ingresado no es valido.",
                                integer=True
                                )
    if codigo_local == "0":
        clear_screen()
        return
    else:
        local_encontrado = []
        codigo_duenio = None
        for local in LOCALES:
            if local['cod'] == codigo_local:
                local_encontrado = local
                codigo_duenio = local['cod_usuario']
                print(codigo_duenio)
                for usuario in USUARIOS:
                    if usuario['cod'] == codigo_duenio:
                        duenio_local_encontrado = usuario
        if local_encontrado:
            print(f"El local seleccionado es {local_encontrado['nombre']}")
            confimacion = input("¿Está seguro que desea eliminar el local seleccionado? (S/N): ")
            if confimacion.lower() == 's':
                LOCALES.remove(local_encontrado)
                USUARIOS.remove(duenio_local_encontrado)
                guardar_archivo(nombre_archivo=NOMBRE_ARCHIVO_LOCALES,datos=LOCALES)
                guardar_archivo(nombre_archivo=NOMBRE_ARCHIVO_USUARIOS,datos=USUARIOS)
                clear_screen()
                print(f"El Local {local_encontrado['nombre']} fue eliminado con éxito.")
            else:
                clear_screen()
                print("La operacion ha sido cancelada.")
        else:
            print("No se ha encontrado el local seleccionado.")
            
def lista_locales():
    clear_screen()
    if LOCALES == []:
        input("No hay locales disponibles. Presione una tecla para volver al menú.")
        clear_screen()
        
    else:
        print("Locales disponibles:")
        print("-------------------------------------------------------------")
        for local in LOCALES:
            if local['estado'] == True:
                estado = 'Activo'
            else:
                estado = 'Inactivo'
            print(f"Código: {local['cod']}, Nombre: {local['nombre']}, Ubicacion: {local['ubicacion']}, Estado: {estado}")
        print("-------------------------------------------------------------")