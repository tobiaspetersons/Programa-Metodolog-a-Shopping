from utils import buscar_cod_maximo, codigo_local_desc, clear_screen, codigo_a_nombre, ingresar_fecha, ingresar_dato, obtener_dia_semana, ingresar_dato_modificado
from datetime import datetime, date
from manejo_archivos import guardar_archivo
from variables_globales import NOMBRE_ACHIVO_PROMOCIONES, PROMOCIONES, LOCALES


def gestion_promociones(usuario_encontrado:list):
    clear_screen()
    while True:
        print("a) Crear descuento para mi local")
        print("b) Modificar descuento de mi local")
        print("c) Eliminar descuento de mi local")
        print("d) Volver")
        opcion_promocion = input("Seleccione una opción (a/b/c/d): ")
        if opcion_promocion == "a":
            crear_promociones(usuario_encontrado=usuario_encontrado)
        elif opcion_promocion == "b":
            modificar_promociones(usuario_encontrado=usuario_encontrado)
        elif opcion_promocion == "c":
            eliminar_promocion()
        elif opcion_promocion == "d":
            clear_screen()
            break
        else:
            print("Opción no válida. Por favor, seleccione a, b, c o d.")

def crear_promociones(usuario_encontrado:list):
    clear_screen()
    cod_promocion = buscar_cod_maximo(PROMOCIONES)
     
    while True:
        nombre_promocion = input('Ingrese el nombre de la nueva promoción (0 para cancelar): ')
        if nombre_promocion == "0":
            clear_screen()
            return
        if nombre_promocion == "":
            print("Ingrese un valor válido.")
        elif any(promo['nombre'] == nombre_promocion for promo in PROMOCIONES):
            print('El nombre de promoción ingresado ya existe.')
            
        else:
            descripcion_promocion = ingresar_dato(mensaje=("Ingrese la descripción de la promoción: "))
            
            fecha_actual = date.today()
            fecha_maxima = datetime(2030, 12, 31).date()
            fecha_inicio_str = ingresar_fecha(
                mensaje= (f"Ingrese la fecha de inicio de la promocion (en formato YYYY-MM-DD (mínimo {fecha_actual})): "),
                fecha_minima= fecha_actual,
                fecha_maxima= fecha_maxima
            )
            fecha_minimo  = datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
            fecha_fin_str = ingresar_fecha(
                mensaje= (f"Ingrese la fecha de inicio de la promocion (en formato YYYY-MM-DD (mínimo {fecha_actual})): "),
                fecha_minima= fecha_minimo,
                fecha_maxima= fecha_maxima
            )
            dia_semana = obtener_dia_semana()

            codigo_local_asociado = codigo_local_desc(usuario_encontrado=usuario_encontrado)
            promocion = {
                'cod': cod_promocion + 1,
                'nombre': nombre_promocion,
                'descripcion': descripcion_promocion,
                'fecha_inicio': fecha_inicio_str,
                'fecha_fin': fecha_fin_str,
                'dia_semana': dia_semana,
                'cod_local' : codigo_local_asociado,
                'estado' : 'Pendiente',
            }
            PROMOCIONES.append(promocion)
            guardar_archivo(nombre_archivo=NOMBRE_ACHIVO_PROMOCIONES,datos=PROMOCIONES)
            clear_screen()
            print("Promoción creada con éxito.")
            break

def modificar_promociones(usuario_encontrado:list):
    clear_screen()
    print("Promociones disponibles:")
    codigo_local_asociado = codigo_local_desc(usuario_encontrado=usuario_encontrado)
    promociones_encontradas = False
    for promocion in PROMOCIONES:
        if promocion['cod_local'] == codigo_local_asociado:
            promociones_encontradas = True
            print(f"Código: {promocion['cod']}, Nombre: {promocion['nombre']}")
    if not promociones_encontradas:
        clear_screen
        print("No se encontraron promociones para su local.")
        return
    codigo_promo = int(input("Ingrese el codigo de la promoción que desea modificar (0 para cancelar): "))
    if codigo_promo == 0:
        clear_screen()
        return
    else:
        clear_screen()
        promo_encontrada = []
        for promocion in PROMOCIONES:
            print (codigo_local_asociado)
            if promocion['cod'] == codigo_promo:
                promo_encontrada = promocion
                break
        if promo_encontrada['estado'] == 'Vencida':
            print("La promoción seleccionada está vencida.")
            modificar_promociones(usuario_encontrado=usuario_encontrado) 
            clear_screen()    
            
        print(f"La promoción seleccionada es {promo_encontrada['nombre']}")
        if promo_encontrada:
            while True:
                print("1. Modificar nombre")
                print("2. Modificar descripcion")
                print("3. Modificar la fecha de inicio")
                print("4. Modificar la fecha de finaliación")
                print("4. Modificar el día de la semana en el que esta válido")
                opcion = int(input("Seleccione una opción (1/2/3/4/5): "))
                clear_screen()
                if opcion == 1:
                    promo_encontrada['nombre'] = ingresar_dato_modificado(
                        mensaje=("Ingrese el nuevo nombre de la promoción: "), 
                        lista=promo_encontrada, 
                        key=('nombre'))
                elif opcion == 2:
                    promo_encontrada['descripcion'] = ingresar_dato_modificado(
                        mensaje=("Ingrese la nueva descripción de la promoción: "), 
                        lista=promo_encontrada, 
                        key=('descripcion'))
                elif opcion == 3:
                    fecha_actual = date.today()
                    fecha_maxima = datetime(2030, 12, 31).date()
                    promo_encontrada['fecha_inicio'] = ingresar_fecha(
                        mensaje= (f"Ingrese la nueva fecha de inicio de la promoción (en formato YYYY-MM-DD (mínimo {fecha_actual})): "),
                        fecha_minima= fecha_actual,
                        fecha_maxima= fecha_maxima
                    )
                elif opcion == 4:
                    fecha_minimo  = datetime.strptime(promo_encontrada['fecha_fin'], "%Y-%m-%d").date()
                    fecha_maxima = datetime(2030, 12, 31).date()
                    promo_encontrada['fecha_inicio'] = ingresar_fecha(
                        mensaje= (f"Ingrese la nueva fecha de finalización de la promoción (en formato YYYY-MM-DD (mínimo {fecha_minimo})): "),
                        fecha_minima= fecha_minimo,
                        fecha_maxima= fecha_maxima
                    )
                elif opcion == 5:
                    promo_encontrada['dia_semana'] = obtener_dia_semana()
                else:
                    print("Opción no valida. Por favor, ingrese 1, 2, 3, 4 o 5")

                guardar_archivo(nombre_archivo=NOMBRE_ACHIVO_PROMOCIONES,datos=PROMOCIONES)
                clear_screen()
                print("Promoción modificada con exito.")
                verificacion = input("¿Desea cambiar otro dato de la promoción? (S/N)")
                if verificacion.lower != "s" or "n":
                    if verificacion.lower() != "s":
                        clear_screen()
                        return
                else:
                    print("Valor no válido. Ingréselo correctamente.")
        else:
            print("No se encontró una promoción con el código ingresado.")


def eliminar_promocion():
    clear_screen()
    codigo_promocion = int(input("Ingrese el codigo de la promoción que quiera eliminar (0 para cancelar): "))
    while True:
        if codigo_promocion == 0:
            clear_screen()
            reporte_promociones_usadas
        else:
            promo_encontrada = []
            for promocion in PROMOCIONES:
                if promocion['cod'] == codigo_promocion:
                    promo_encontrada = promocion
                    break
            if promo_encontrada:
                print(f"La promoción seleccionada es {promo_encontrada['nombre']}")
                confimacion = input("¿Está seguro que desea eliminar la promoción seleccionada? (S/N): ")
                if confimacion.lower() == 's':
                    PROMOCIONES.remove(promo_encontrada)
                    guardar_archivo(nombre_archivo=NOMBRE_ACHIVO_PROMOCIONES,datos=PROMOCIONES)
                    print(f"La promoción {promo_encontrada['nombre']} fue eliminada con éxito.")
                else:
                    print("La operacion ha sido cancelada.")
            else:
                print("No se ha encontrado la promoción seleccionada.")
            
    
def solicitudes_promociones_admin():
    clear_screen()
    print("Solicitudes de Descuentos Pendientes:")
    promociones_pendientes = []
    for promo in PROMOCIONES:
        if promo['estado'] == "Pendiente":
            promociones_pendientes.append(promo)

    if not promociones_pendientes:
        clear_screen()
        print("No hay solicitudes pendientes de aprobación.")
    else:
        for promocion in promociones_pendientes:
            print(f"Local que propone la promoción: {codigo_a_nombre(codigo = promocion['cod_local'])}")
            print(f"Código: {promocion['cod']}")
            print(f"Nombre: {promocion['nombre']}")
            print(f"Descripción: {promocion['descripcion']}")
            print(f"Fecha de inicio: {promocion['fecha_inicio']}")
            print(f"Fecha de finalización: {promocion['fecha_fin']}")    
            print(f"Dia de la semana: {promocion['dia_semana']} ") 
            
            decision = input("¿Desea aprobar esta solicitud? (S/N): ").strip().lower()
            if decision == 's':
                promocion['pendiente_aprobacion'] = False
                promocion['estado'] = 'Activa' 
                clear_screen()
                print("Solicitud aprobada.")
            elif decision == 'n':
                promocion['pendiente_aprobacion'] = False
                promocion['estado'] = 'Rechazada'
                clear_screen()
                print("Solicitud denegada.")
            else:
                print("Opción no válida. La solicitud no se ha modificado.")
        guardar_archivo(nombre_archivo=NOMBRE_ACHIVO_PROMOCIONES, datos=PROMOCIONES)

    
#FUNCION REPORTE DE UTILIZACION DESCUENTOS
def reporte_promociones_usadas():
        pass
    
#FUNCION BUSCAR DESCUENTOS DE LOCALES
def usar_promociones_cliente():
    fecha_dia = date.today()
    dia_semana = fecha_dia.weekday()
    nombre_local = input("Ingrese el nombre del local para ver sus promociones (ingrese '0' para volver al menú): ").strip().lower()
    if nombre_local == '0':
        return
    
    codigo_local = 0
    for local in LOCALES:
        if nombre_local == local['nombre'].lower():
            codigo_local = local['cod']
            break
        
    if codigo_local != 0:
        i = 1
        promociones_disponibles = []
        for promo in PROMOCIONES:
            fecha_inicio = promo['fecha_inicio']
            fecha_fin = promo['fecha_fin']
            if (
                codigo_local == promo['cod_local']
                and promo['estado'] == "Activa" 
                and date.today() >= datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
                and date.today() <= datetime.strptime(fecha_fin, "%Y-%m-%d").date()
                and dia_semana == promo['dia_semana']
            ):
                print(f"Promoción número {i}: ")
                print(f"Nombre de la promoción: {promo['nombre']}")
                print(f"Descripción de la promoción: {promo['descripcion']}")
                promociones_disponibles.append([i, promo['cod'], promo['nombre']])
                i += 1
                
        if i == 1:
            print("No hay promociones disponibles en el día de hoy para este local.")
        else:
            promocion = int(input("Ingrese el número de promoción que desea aplicar a su compra: "))
            for promo in promociones_disponibles:
                if promocion == promo[0]:
                    print (f"La promoción seleccionada es: {promo[2]}")   
    else:
        print("No se encontró un local con el nombre ingresado.")
        print("Locales disponibles:")
        for local in LOCALES:
            print(f"Código: {local['cod']}, Nombre: {local['nombre']}")
            

    
            
            