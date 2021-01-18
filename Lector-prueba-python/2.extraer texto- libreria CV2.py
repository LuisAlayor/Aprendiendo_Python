#https://www.youtube.com/watch?v=OutxRdkNOK4&ab_channel=TruzzBlogg#
import pytesseract
import cv2
from PIL import Image


#implementamos el prograla al codigo
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

im = cv2.imread("C:/Users/usuario/Desktop/Lector-prueba-python/example.png")
txt = pytesseract.image_to_string(im)

print(txt)

#Display original image
cv2.imshow("Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()

#primero has de cerrar la imagen para que cree el txt
mi_archivo = open("prueba1.txt", "w")
mi_archivo.write(txt + "\n")
mi_archivo.close()
