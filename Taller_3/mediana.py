numeros = []
valor_M = int(input())
medianas = []

while True:
    datos = int(input())
    if datos==0:
        break

    numeros.append(datos)
    if len(numeros)!=0 and (len(numeros) % valor_M == 0):
        numeros.sort()

        if len(numeros) % 2 == 0:
            suma = numeros[len(numeros)//2] + numeros[(len(numeros)//2) - 1]
            if suma % 2 == 0:
                medianas.append(suma//2)
            else:
                fraccion = f'{suma}/2'
                medianas.append(fraccion)
        
        else:
            mediana = numeros[len(numeros)//2]
            medianas.append(mediana)
    
for mediana in medianas:
    print(mediana)