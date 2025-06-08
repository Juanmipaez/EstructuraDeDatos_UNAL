Lista_numeros = []


while True:
    datos = input()
    if datos=="E":
        break
    datos = datos.split(" ")
    if (datos[0]=="A" and datos[1] not in Lista_numeros ):
        Lista_numeros.append(int(datos[1]))
    
    elif (datos[0]=="M"):
        suma = 0
        for num in Lista_numeros:
            if num % int(datos[1]) == 0:
                suma+=num
        print(suma)