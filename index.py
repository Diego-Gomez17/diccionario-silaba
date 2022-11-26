# motor de busqueda
import re
archivo = './diccionario.txt'

salida = "./result.txt"
palabra = input("Ingresa búsqueda: ")


def buscador(palabra, archivo):
    lista = []
    patron = re.compile(r"(\w+)")
    palabra = palabra.lower()
    with open(archivo, "r") as file:
        lista = [linea.rstrip() for linea in file if palabra in patron.findall(linea.lower())]
        
    return lista

lista = buscador(palabra, archivo)
frase= lista[0]
secuencia=r"(\w*{}\w*)".format(palabra)
#secuencia=r"([{}])".format(palabra)
busqueda= re.findall(secuencia,frase)
print (busqueda)


# result=list(lista[0])
result = lista
#print(result)

