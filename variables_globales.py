from manejo_archivos import leer_archivo

NOMBRE_ARCHIVO_USUARIOS = 'usuarios.json'
NOMBRE_ARCHIVO_LOCALES = 'locales.json'
NOMBRE_ACHIVO_PROMOCIONES = 'promociones.json'
NOMBRE_ARCHIVO_USO_PROMOCIONES = 'uso_promociones.json'

USUARIOS = leer_archivo(nombre_archivo=NOMBRE_ARCHIVO_USUARIOS)
LOCALES = leer_archivo(nombre_archivo=NOMBRE_ARCHIVO_LOCALES) 
PROMOCIONES = leer_archivo(nombre_archivo=NOMBRE_ACHIVO_PROMOCIONES)
USO_PROMOCIONES = leer_archivo(nombre_archivo=NOMBRE_ARCHIVO_USO_PROMOCIONES)