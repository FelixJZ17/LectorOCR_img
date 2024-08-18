import os

def obtener_paths_imagenes(directorio):
    paths_imagenes = []

    # Recorre todos los archivos en el directorio
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.lower().endswith('.jpg'):  # Filtra solo archivos .jpg
                # Almacena el path completo de la imagen en la lista
                paths_imagenes.append(os.path.join(root, file))
            elif file.lower().endswith('.png'):  # Filtra solo archivos .png
                # Almacena el path completo de la imagen en la lista
                paths_imagenes.append(os.path.join(root, file))

    return paths_imagenes