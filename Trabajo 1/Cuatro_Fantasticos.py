lista_primos = [2,3,5,7]
divisores = []
numero = int(input())

for primo in lista_primos:
    if (numero%primo == 0):
        divisores.append(primo)

if len(divisores)>0:
    print(f'es multiplo de {min(divisores)}')
else:
    print(f'no es multiplo de ninguno de los primeros cuatro primos')