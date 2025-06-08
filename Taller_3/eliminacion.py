numeros = []

while True:
    datos = int(input())
    if datos == 0:
        break
    
    if datos in numeros:
        numeros.remove(datos)
    elif (datos+1) in numeros:
        numeros.remove(datos+1)
    elif (datos-1) in numeros:
        numeros.remove(datos-1)
    else:
        numeros.append(datos)

if len(numeros)==0:
    print(0)
else:
    for i in numeros:
        print(i, end=" " if i != numeros[-1] else "")