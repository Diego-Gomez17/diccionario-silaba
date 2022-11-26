import re

archivo='./diccionario.txt'
#palabra = input("Ingresa búsqueda: ")
silaba=['ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de', 'di', 'do', 'du', 'fa', 'fe', 'fi', 'fo', 'ga', 'ge', 'gi', 'go', 'ja', 'je', 'ji', 'jo', 'ju', 'la', 'le', 'li', 'lla', 'lle', 'llo', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu', 'que', 'qui', 'ra', 're', 'ri', 'ro', 'ru', 'sa', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'ya', 'ye', 'yo']


for1=0
for2=0
result=[]
for sila in silaba:
    secuencia=r"('^{}\w')".format(sila)
    with open(archivo, "r") as file:
        for elemento in file:
            if re.findall(('^{}\w').format(sila),elemento):
                #print(elemento)
                count= elemento.split(" ",1)
                result.append(count[0])
            
        print(secuencia)

resultado= str(result)
file = open('./SilabasLocas.txt','w')
file.write(resultado)
file.close