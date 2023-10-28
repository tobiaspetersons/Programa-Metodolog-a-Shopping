from administrador import menu_administrador
from cliente import menu_cliente
from duenio_local import menu_duenio
from manejo_archivos import guardar_archivo
from utils import validar_correo, buscar_cod_maximo,clear_screen, enviar_correo, generar_codigo_confirmacion
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
        
def registrar_cliente():
    while True:
        correo = input("Ingrese un email para registrarse (0 para cancelar): ")
        if correo == "0":
            return
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
    clave = input("Ingrese una clave: ")
    while clave == "":
        print("Ingrese un valor valido")
        clave = input("Ingrese una clave: ")
        
    codigo_confirmacion = generar_codigo_confirmacion()
    asunto = ("Confirmación de Registro")
    mensaje = (f"Gracias por registrarte. Tu código de confirmación es: {codigo_confirmacion}")
    enviar_correo(destinatario=correo,asunto=asunto,mensaje=mensaje)
    while True:
        codigo_confirmacion_ingresado = input("Ingrese el código de confirmación que le enviamos a su correo: ")
        if codigo_confirmacion_ingresado == codigo_confirmacion:
            nuevo_usuario = {
            'cod': codigo_cliente + 1,
            'email': correo_cliente,
            'clave': clave,
            'rol': "cliente"
            }
            USUARIOS.append(nuevo_usuario)
            guardar_archivo(nombre_archivo=NOMBRE_ARCHIVO_USUARIOS, datos= USUARIOS)
            clear_screen()
            print(f"Cliente registrado con ID {nuevo_usuario['cod']}")
            break
        else:
            clear_screen()
            print("Código de confirmación incorrecto. Intente nuevamente.")
        
    
    
    
    