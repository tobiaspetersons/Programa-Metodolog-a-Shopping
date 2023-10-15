import os
import json
from typing import Optional

def leer_archivo(nombre_archivo:str)->list:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            response = json.load(archivo)
    else:
        response = [] 
    return response

def guardar_archivo(nombre_archivo:str, datos:Optional[list|dict]):
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
