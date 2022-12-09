import re
# crea un diccionario filtrado por palabras que comience con "silaba"
archivo='./diccionario.txt'
silaba=['ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de', 'di', 'do', 'du', 'fa', 'fe', 'fi', 'fo', 'ga', 'ge', 'gi', 'go', 'ja', 'je', 'ji', 'jo', 'ju', 'la', 'le', 'li', 'lla', 'lle', 'llo', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu', 'que', 'qui', 'ra', 're', 'ri', 'ro', 'ru', 'sa', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'ya', 'ye', 'yo']

result=[]
anular="\n"
for sila in silaba:
    secuencia=r"('^{}\w')".format(sila)
    with open(archivo, "r") as file:
        for elemento in file:
            if re.findall(('^{}\w').format(sila),elemento):
                owo= elemento.replace(".","")
                owo= owo.replace(")","")
                owo= owo.replace(").","")
                owo= owo.replace("1","")
                owo= owo.replace("2","")
                owo= owo.replace("2","")
                owo= owo.replace("->","")
                owo= owo.replace(",","")
                owo= owo.replace("\n","")
                count= owo.split(" ",1)
                result.append(count[0])
        print(secuencia)
contador=0
for x in silaba:
    for i in result:
        if re.findall(('^{}\w').format(x),i):
            contador=contador+1
    if contador < 200:
        dowo="hay ",contador," tantas palabras con: ",x, " tiene 5 Estrellas"
    if contador >=200 and contador <= 800:
        dowo="hay ",contador," tantas palabras con: ",x, " tiene 4 Estrellas"
    if contador >=800 and contador <= 1000:
        dowo="hay ",contador," tantas palabras con: ",x, " tiene 3 Estrellas"
    if contador >=1000 and contador <= 3000:
        dowo="hay ",contador," tantas palabras con: ",x, " tiene 2 Estrellas"
    if contador > 3000:
        dowo="hay ",contador," tantas palabras con: ",x, " tiene 1 Estrellas"
    
    print(dowo)
    contador=0