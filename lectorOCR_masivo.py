from pathsJPG import obtener_paths_imagenes
from moverficheros import mover_imagenes
from escribirExcel import escribir_excel
import cv2  ## openCV
import pytesseract

# Cargar imagenes
directorio_imagenes  = "imgSinProcesar/"

# Llama a la función y almacena los resultados en una lista
lista_paths = obtener_paths_imagenes(directorio_imagenes)

# Compruebo si hay imagenes en la lista y si no hay devuelvo string. 
if not lista_paths:
    print("No hay imagenes pendientes de procesar")
else:
    # Si hay imagenes en la carpeta, hago un for que recorre todo y lo guarda en la excel
    for imagen in lista_paths:
        img = cv2.imread(imagen)

        # Convertir imagen a escala de grises y mostrar preview
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Aplicar umbral para convertir a imagen binaria
        threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) [1]
        cv2.startWindowThread()
        
        # Cambiar directorio donde esta instalado tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

        # Pasar la imagen a traves de pytesseract
        text = pytesseract.image_to_string(threshold_img)

        cv2.imshow("gray-Preview", gray)
        
        #Save the extratec text in an Excel file (escribirExcel.py)
        texto_modificado = text.replace('\n', '  ;  ')
        escribir_excel(texto_modificado)

## Mueve los ficheros de sitio, ahora que han sido procesados
directorio_destino = 'imgProcesadas/'
mover_imagenes(lista_paths, directorio_destino)

