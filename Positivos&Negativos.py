numero = int(input())
suma_pos = 0
suma_neg = 0
for i in range(numero):
    numero_2 = int(input())
    if numero_2 >= 0:
        suma_pos+=numero_2
    else:
        suma_neg+=numero_2
print(f'positivos {suma_pos}, negativos {suma_neg}')