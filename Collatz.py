numero = int(input())
print(numero)

while True:
    if (numero%2 == 0):
        numero = numero/2
        print(int(numero))
        if numero==1:
            break
    elif (numero==1):
        break
    else:
        numero = (3*numero) + 1
        print(int(numero))

