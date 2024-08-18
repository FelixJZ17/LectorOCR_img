import cv2  ## openCV
import pytesseract

# Cargar imagen
PathPrincipal = ""
img = cv2.imread("imgSinProcesar/ejemplo.jpg")

# Convertir imagen a escala de grises y mostrar preview
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.startWindowThread()
cv2.namedWindow("gray-Preview")

# Aplicar umbral para convertir a imagen binaria
threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) [1]
cv2.startWindowThread()
cv2.namedWindow("threshold-Preview")
cv2.waitKey(0)

# Cambiar directorio donde esta instalado tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Pasar la imagen a traves de pytesseract
text = pytesseract.image_to_string(threshold_img)

cv2.imshow("gray-Preview", gray)
cv2.imshow("threshold-Preview", threshold_img)
cv2.waitKey(0)

#Print the extratec text
print(text)
