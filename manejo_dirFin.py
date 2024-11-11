import os
from pathlib import Path

# Paso 1: Definir ruta de la carpeta y archivo
carpeta_ruta = "proyecto"
archivo_ruta = os.path.join(carpeta_ruta, "notas.txt")

# Paso 2: Crear carpeta si no existe
if not os.path.exists(carpeta_ruta):
    os.makedirs(carpeta_ruta)
    print("Se ha creado la carpeta 'proyecto'.")

# Paso 3: Crear archivo y escribir en él si no existe
if not os.path.exists(archivo_ruta):
    with open(archivo_ruta, "w") as archivo:
        archivo.write("Esta es la primera nota en el archivo.\n")
    print("Se ha creado el archivo 'notas.txt' y se ha escrito texto en él.")
else:
    print("El archivo 'notas.txt' ya existe.")

# Paso 4: Leer y mostrar el contenido actual del archivo
with open(archivo_ruta, "r") as archivo:
    contenido = archivo.read()
print("Contenido actual del archivo 'notas.txt':\n", contenido)

# Paso 5: Anexar más texto y leer nuevamente
with open(archivo_ruta, "a") as archivo:
    archivo.write("\nEsta es una nueva línea agregada al archivo.")
print("Se ha agregado más texto al archivo 'notas.txt'.")

# Leer el contenido actualizado
with open(archivo_ruta, "r") as archivo:
    contenido_actualizado = archivo.read()
print("Contenido actualizado del archivo 'notas.txt':\n", contenido_actualizado)
