numero_a = int(input())
numero_b = int(input())
contador = 1

while True:
    potencia = numero_a**contador
    if potencia <= numero_b:
        print(potencia)
        contador+=1
    else:
        break
