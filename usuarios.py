import re
from administrador import menu_administrador
from cliente import menu_cliente
from duenio_local import menu_duenio
from manejo_archivos import guardar_archivo
from utils import validar_correo, buscar_cod_maximo,clear_screen, enviar_correo, generar_codigo_confirmacion, ingresar_dato, ingresar_num_formato, ingresar_clave
from variables_globales import USUARIOS, NOMBRE_ARCHIVO_USUARIOS

def iniciar_sesion():
    usuario_input = input("Ingrese su email: ")
    clave_input = input("Ingrese su clave: ")
    usuario_encontrado = []
    for usuario in USUARIOS:
        if usuario['email'] == usuario_input and usuario['clave'] == clave_input:
            usuario_encontrado = usuario
            break
    if usuario_encontrado:
        if usuario_encontrado['rol'] == "admin":
            menu_administrador()
        elif usuario_encontrado['rol'] == "duenio_local":
            menu_duenio(usuario_encontrado=usuario_encontrado)
        elif usuario_encontrado['rol'] == "cliente":
            menu_cliente(usuario_encontrado=usuario_encontrado)
    else:
        clear_screen()
        print("No existe ese usuario o contraseña")
        
def registrar(rol='cliente',mensaje_nombre="Ingrese su nombre (0 para cancelar): "):
    while True:
        nombre = ingresar_dato(mensaje_nombre)
        if nombre == "0":
            return
        apellido = ingresar_dato(mensaje="Ingrese su apellido: ")
        correo = input("Ingrese un email para registrarse: ")
        mails_repetidos = []
        for usuario in USUARIOS:
            if correo == usuario['email']:
                mails_repetidos.append(usuario)
        if mails_repetidos == []:
            if validar_correo(correo):
                correo_cliente = correo
                break
            else:
                clear_screen()
                print("Formato de correo electrónico no válido. Intente nuevamente.")
        else: 
            clear_screen()
            print("Email ya registrado. Intente nuevamente.")
    codigo_cliente = buscar_cod_maximo(archivo=USUARIOS)
    clave = ingresar_clave()
    dni = ingresar_num_formato(mensaje="Ingrese su DNI: ",
                               cant=8,
                               mensaje_error="Formato de DNI no valido. Intente nuevamente."
                               )
    telefono = ingresar_num_formato(mensaje="Ingrese su número de teléfono: ",
                                    cant=10,
                                    mensaje_error="Formato de número de telefono no válido. Intente nuevamente"
                                    )
    codigo_confirmacion = generar_codigo_confirmacion()
    asunto = ("Confirmación de Registro")
    mensaje = (f"Gracias por registrarte. Tu código de confirmación es: {codigo_confirmacion}")
    enviar_correo(destinatario=correo,asunto=asunto,mensaje=mensaje)
    while True:
        codigo_confirmacion_ingresado = input("Ingrese el código de confirmación que le enviamos a su correo: ")
        if codigo_confirmacion_ingresado == codigo_confirmacion:
            nuevo_usuario = {
            'cod': codigo_cliente + 1,
            'nombre': nombre,
            'apellido': apellido,
            'email': correo_cliente,
            'clave': clave,
            'rol': rol,
            'dni': dni,
            'telefono': telefono
            }
            USUARIOS.append(nuevo_usuario)
            guardar_archivo(nombre_archivo=NOMBRE_ARCHIVO_USUARIOS, datos= USUARIOS)
            clear_screen()
            if nuevo_usuario['rol']=='admin':
                print(f"Administrador registrado con ID {nuevo_usuario['cod']}")
            else:
                print(f"Cliente registrado con ID {nuevo_usuario['cod']}")
            break
        else:
            clear_screen()
            print("Código de confirmación incorrecto. Intente nuevamente.")
        
    
    
    
    