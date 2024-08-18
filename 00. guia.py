### Video de seguimiento: https://www.youtube.com/watch?v=eFpqjFPLR78

### Pasos para hacer funcionar el proyecto:
### 1. Instalar Tesseract en Windows  --> https://github.com/UB-Mannheim/tesseract/wiki
###    - En la instalación, elegir los idiomas que queremos, English viene por defecto. 
###    - Elijo Spanish en la propio instalación. 

###    - Guardar la ruta de instalación para luego usar el programa, en mi caso:
###        >C:/Program Files/Tesseract-OCR/tesseract.exe

### 2. Luego de la instalación agregamos el path a las variables de entornos. 
###     - Para el usuario {FJges}, al path, en mi caso agrego para que reconozca los pip install
###        >C:\Users\FJges\AppData\Local\Programs\Python\Python312\Scripts\
###        >C:\Users\FJges\AppData\Local\Programs\Python\Python312\

###     - Además, en variables del sistema, al path, agrego los mismo:
###        >C:\Users\FJges\AppData\Local\Programs\Python\Python312\Scripts\
###        >C:\Users\FJges\AppData\Local\Programs\Python\Python312\

### 3. Ahora con eso hago un pip install de la librería de Tesseract con (desde el cmd): 
###        >pip install pytesseract

###    Lo mismo con la libreria de OpenCV:
###        >pip install opencv-python

### 4. Si se ha instalado correctamente y me sale el mensaje. Ya lo puedo usar en Python. 
###    Para usarlo en nuestro codigo, importamos las librerías en nuestro fichero.py:
###         >import cv2
###         >import pytesseract

## 5. A partir de aquí, seguir el codigo del programa .py. 