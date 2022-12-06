anular="\n"
lista=[]
print(anular)
with open("result.txt", "r") as archivo:
    for owo in archivo:
        lista.append(owo.replace("\n"," "))
file = open('./final.txt','w')
file.write(str(lista))
file.close
