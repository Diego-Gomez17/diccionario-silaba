import PyPDF2
import os

#extrae el texto del pdf

pdfFileObj = open('./dic.pdf','rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#cantidad de paginas
print("Cantidad de paginas: ", pdfReader.numPages)

# obtener contido del documento


read=" "
for x in range(3595,32055):
    pageObj= pdfReader.getPage(x)
    read=read+pageObj.extractText()


file = open('./diccionario.txt','w')
file.write(read)
file.close


# with open(salida, "w") as archivo_salida:
#     for linea in lineas_escribir:
#         archivo_salida.write(linea + "\n")