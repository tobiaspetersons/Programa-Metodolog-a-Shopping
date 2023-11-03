from traceback import print_exc
from typing import Union
import re
import os
from datetime import datetime, date
from random import random, randint
import qrcode
import tempfile
from PIL import Image, ImageTk
import tkinter as tk
from typing import List
import smtplib #mail
from tabulate import tabulate
from manejo_archivos import guardar_archivo
from variables_globales import NOMBRE_ACHIVO_PROMOCIONES, LOCALES, PROMOCIONES, USO_PROMOCIONES, NOMBRE_ARCHIVO_USO_PROMOCIONES, USUARIOS

def str2number(text: str,
               print_exception: bool = True) -> Union[None, int, float]:
    """ Función que transforma un texto en un entero.

    Args:
        texto (str): Texto con formato de entero.
        print_exception (bool): Si esta en True muestra el mensaje de la excepción.

    Returns:
        Union[None, int, float]: Retorna un entero o None en caso de error.
    """
    try:
        return int(text.strip())
    except Exception as ex:
        try:
            return float(text.strip())
        except Exception as ex:
            if print_exception:
                print_exc()
    return None

def input_number(message: str,
                 error_message: str,
                 integer: bool = False,
                 repeat: bool = True) -> Union[None, int, float]:
    """ Se utiliza para ingresar un número.

    Args:
        message (str): Texto que muestra el input.
        error_message (str): Texto que se muestra en caso de error.
        integer (bool): Se está en True retorna un entero, en caso contrario
            retorna un flotante. Defaults to False.
        repeat (bool): Si está en True obliga a que se ingrese un número.
        
    Returns:
        Union[None, int, float]: Retorna un None, int o float.
    """
    while True:
        input_data = input(message)
        data = str2number(text=input_data, print_exception=False)
        if data is not None:
            return int(data) if integer else float(data)
        else:
            if error_message is not None and len(error_message) > 0:
                print(error_message + f"[{input_data}]")
        if not repeat:
            return None


def buscar_cod_maximo(archivo, key='cod'):
    """ Busca el código máximo

    Args:
        archivo (list): recibe una lista de diccionarios
        key (str): recibe el nombre de la llave a buscar dentro de cada diccionario

    Returns:
        int: devuelve el código máximo de la lista de diccionarios, según la key
    """
    max_codigo = max([registro[key] for registro in archivo], default=0)
    return max_codigo

def codigo_local_con_usuario(usuario_encontrado:list):
    for local in LOCALES:
        if usuario_encontrado['cod'] == local['cod_usuario']:
            codigo_local = local['cod']
            return codigo_local
        
def codigo_cliente(usuario_encontrado:list):
    for usuario in USUARIOS:
        if usuario_encontrado['cod'] == usuario['cod']:
            codigo_cliente = usuario['cod']
            return codigo_cliente
        
def nombre_a_codigo(input_nombre):
    for local in LOCALES:
        if local['nombre'] == input_nombre:
            return local['cod']
    return None  
        
def codigo_a_nombre(codigo:int)->str:
    for local in LOCALES:
        if codigo == local['cod']:
            nombre_local = local['nombre']
            return nombre_local
        
def clear_screen():
    if 'nt' in os.name:
        _ = os.system("cls")
    else:
        _ = os.system("clear")
        
def validacion_palabras(variable:str):
    if variable == "":
        print ('Ingrese un valor valido.')
        return True

def validar_correo(correo:str):
    # Patrón para validar un correo electrónico
    patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(patron_correo, correo):
        return True
    else:
        return False

def validar_dia_semana(dia:str):
    dias_semana_validos = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"]
    if dia.lower() in dias_semana_validos:
        return True
    else:
        return False

def verificar_vencimiento_promos():
    fecha_hoy = date.today()
    for promo in PROMOCIONES:
        if promo['estado'] == 'Activa':
            fecha_fin_promo= datetime.strptime(promo['fecha_fin'], "%Y-%m-%d").date()
            if fecha_hoy > fecha_fin_promo:
                promo['estado'] = 'Vencida'
                guardar_archivo(nombre_archivo=NOMBRE_ACHIVO_PROMOCIONES,datos=PROMOCIONES)


def validar_nombre(nuevo_nombre: str, lista_nombres: List[str]) -> str:
    if not nuevo_nombre:
        return "El nombre no puede estar vacío."
    if nuevo_nombre in lista_nombres:
        return "El nombre ya está en uso."
    return ""
            
def ingresar_dato(mensaje:str)->str:
    valor = input(mensaje)
    while True:
        if valor == "":
            print ("Ingrese un valor valido.")
            valor = input(mensaje)
        else:
            return valor
        
def ingresar_num_formato(mensaje:str, cant:int, mensaje_error:str)->int:
    while True:
        valor = input_number(message=mensaje,
                         error_message="Ingrese un valor valido.",
                         integer=True
                        )
        if len(str(valor)) == cant:  
            return valor
        else:
            print(mensaje_error)
    
def ingresar_dato_modificado(mensaje:str, lista:list, key:str)->str:
    valor = input(mensaje)
    while valor == "":
        print ("Ingrese un valor valido.")
        valor = input(mensaje)
    while valor == lista[key]:
        print ("Ingrese un valor distinto al actual.")
        valor = input(mensaje)
    return valor

def ingresar_clave():
    while True:
        clave = input("Ingrese una clave: ")
        if (len(clave) >= 8 and re.search(r"[A-Z]", clave) and 
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", clave)):
            return clave
        else:
            print("La clave debe tener al menos 8 caracteres, al menos una mayúscula y al menos un carácter especial. Intente nuevamente.")

def ingresar_correo():
    while True:
        correo = input("Ingrese el correo electronico del dueño: ")
        if validar_correo(correo):
            email_nuevo_duenio = correo
            return email_nuevo_duenio
        else:
            print("Formato de correo electrónico no válido. Intente nuevamente.")
            
def ingresar_correo_duenio(mensaje: str) -> str:
    while True:
        correo = input(mensaje + " (solo necesita agregar la parte antes de '@shopping.com'): ")
        correo = correo + "@shopping.com"  
        if validar_correo(correo):
            return correo
        else:
            print("Formato de correo electrónico no válido. Intente nuevamente.")
            
def ingresar_fecha_cliente(mensaje:str)->date:
    while True:
        try:
            fecha = datetime.strptime(input(mensaje), '%d-%m-%Y').date()
            return fecha.strftime('%d-%m-%Y')
        except ValueError:
            print("Formato de fecha inválido. Intente nuevamente.")
            
def ingresar_fecha(mensaje: str, fecha_minima: date, fecha_maxima: date) -> date:
    while True:
        try:
            fecha = datetime.strptime(input(mensaje), '%d-%m-%Y').date()
            if fecha < fecha_minima:
                print(f"La fecha ingresada debe ser mayor o igual a {fecha_minima}.")
                continue
            elif fecha > fecha_maxima:
                print(f"La fecha ingresada debe ser menor o igual a {fecha_maxima}.")
                continue
            else:
                return fecha.strftime('%d-%m-%Y')
        except ValueError:
            print("Formato de fecha inválido. Intente nuevamente.")


            
def obtener_dia_semana():
    dias_semana = {
        "lunes": 0,
        "martes": 1,
        "miércoles": 2,
        "jueves": 3,
        "viernes": 4,
        "sábado": 5,
        "domingo": 6
    }
    while True:
        dia_nombre = input("Ingrese el nombre del día de la semana en el que es válida la promoción: ").lower()
        if dia_nombre in dias_semana:
            dia_semana = dias_semana[dia_nombre]
            return dia_semana
        else:
            print("Nombre de día de la semana no válido. Inténtelo de nuevo.")

def generar_codigo_confirmacion():
    codigo = ""
    for i in range(6):
        codigo += str(randint(0, 9))
    return codigo

def enviar_correo(destinatario, asunto, mensaje):
    try:
        #configura el servidor smtp de gmail
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "shoppingmetodologia@gmail.com"
        smtp_password = "uwyc eqwf iimo ugfa"
        #crea una conexion con el servidor
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        #crea el mensaje
        cuerpo_del_mensaje = f"Subject: {asunto}\n\n{mensaje}"
        cuerpo_del_mensaje = cuerpo_del_mensaje.encode('utf-8')
        #envia el mensaje
        server.sendmail(smtp_username, destinatario, cuerpo_del_mensaje)
        #cierra la conexion
        server.quit()
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {str(e)}")
        
def mostrar_tabla(data, headers):
    table = tabulate(data, headers, tablefmt="fancy_grid")
    print(table)

def generar_codigo_qr(promocion:list,usuario_encontrado:list):
    nro_random = f"123{randint(0, 9999999):03}"
    codigo_qr = f"{promocion['nombre']}-{promocion['cod']}-{promocion['cod_local']}-{nro_random}"
    fecha_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    cod_cliente = codigo_cliente(usuario_encontrado=usuario_encontrado)
    img = qrcode.make(codigo_qr)
    with tempfile.NamedTemporaryFile(delete=False) as f:
        img.save(f.name, format='PNG')
        root = tk.Tk()
        root.title("Código QR")
        img = ImageTk.PhotoImage(Image.open(f.name))
        label = tk.Label(root, image=img)
        label.pack()
        root.mainloop()
    uso_promocion = {
        'nombre': promocion['nombre'],
        'cod_local' : promocion['cod_local'],
        'cod_cliente' : cod_cliente,
        'fecha_hora': fecha_hora,
        'codigo_utilizado': f"{promocion['nombre']}-{promocion['cod']}-{promocion['cod_local']}-{nro_random}"
        
    }
    USO_PROMOCIONES.append(uso_promocion)
    guardar_archivo(nombre_archivo=NOMBRE_ARCHIVO_USO_PROMOCIONES, datos=USO_PROMOCIONES)
        

