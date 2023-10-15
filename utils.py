import re
import os
from datetime import datetime, date
from dateutil import parser
import random 
import string 
from typing import List
import smtplib #mail
from manejo_archivos import guardar_archivo
from variables_globales import NOMBRE_ACHIVO_PROMOCIONES, LOCALES, PROMOCIONES


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

def codigo_local_desc(usuario_encontrado:list):
    for local in LOCALES:
        if usuario_encontrado['cod'] == local['cod_usuario']:
            codigo_local = local['cod']
            return codigo_local
        
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

def validar_fecha(fecha_str:str):
    try:
        fecha = parser.parse(fecha_str)
        return True
    except ValueError:
        return False

def validar_formato_fecha(fecha:str):
    # Patrón para validar el formato de fecha YYYY-MM-DD
    patron_fecha = r'^\d{4}-\d{2}-\d{2}$'

    if re.match(patron_fecha, fecha):
        return True
    else:
        return False

def validar_rango_fecha(fecha, fecha_minima, fecha_maxima):
    fecha_ingresada = datetime.strptime(fecha, "%Y-%m-%d").date()
    if fecha_minima <= fecha_ingresada <= fecha_maxima:
        return True
    else:
        return False
    
def validar_dia_semana(dia):
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
    while valor == "":
        print ("Ingrese un valor valido.")
        valor = input(mensaje)
        return valor
    
def ingresar_dato_modificado(mensaje:str, lista:list, key:str)->str:
    valor = input(mensaje)
    while valor == "":
        print ("Ingrese un valor valido.")
        valor = input(mensaje)
    while valor == lista[key]:
        print ("Ingrese un valor distinto al actual.")
        valor = input(mensaje)
    return valor

def ingresar_correo():
    while True:
        correo = input("Ingrese el correo electronico del dueño: ")
        if validar_correo(correo):
            email_nuevo_duenio = correo
            return email_nuevo_duenio
        else:
            print("Formato de correo electrónico no válido. Intente nuevamente.")

def ingresar_fecha(mensaje:str, fecha_minima:datetime, fecha_maxima:datetime):
    print(type(fecha_maxima))
    while True:
        fecha = input(mensaje)
        if validar_fecha(fecha):
            if validar_formato_fecha(fecha):
                    if validar_rango_fecha(fecha=fecha, fecha_minima=fecha_minima, fecha_maxima=fecha_maxima):
                        return fecha
                    else:
                        print("La fecha no está dentro del rango permitido.")
            else:
                print("Formato de fecha no válido. Intente nuevamente.")
        else: 
            print("Ingrese una fecha valida.")
            
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
    return ''.join(random.choices(string.digits, k=6))

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
