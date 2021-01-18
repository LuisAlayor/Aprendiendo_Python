#https://www.youtube.com/watch?v=OutxRdkNOK4&ab_channel=TruzzBlogg#
import pytesseract
from PIL import Image

#implementamos el prograla al codigo
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

im = Image.open("C:/Users/usuario/Desktop/Lector-prueba-python/example.png")
txt = pytesseract.image_to_string(im)

#añadimos esta liner para lograr que 
#la imagen se abra cuando se ejecute el programa
im.show()

print(txt)

mi_archivo = open("prueba_1.txt", "w")
mi_archivo.write(txt + "\n")
mi_archivo.close()
