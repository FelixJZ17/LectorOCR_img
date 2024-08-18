import os
import shutil

def mover_imagenes(lista_paths, directorio_destino):
    for path in lista_paths:
        # Obtiene el nombre del archivo
        nombre_archivo = os.path.basename(path)
        # Crea la ruta completa en el directorio de destino
        destino = os.path.join(directorio_destino, nombre_archivo)
        # Mueve el archivo al nuevo directorio
        shutil.move(path, destino)
        print(f"Movido: {path} -> {destino}")