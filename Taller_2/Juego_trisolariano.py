cantidad_de_numeros = int(input())
numeros_SO = tuple(map(int,input().split(",")))
numeros_LAR = tuple(map(int,input().split(",")))
numeros_IS = tuple(map(int,input().split(",")))

puntos_SO = 0
puntos_LAR = 0
puntos_IS = 0

for i in range(cantidad_de_numeros):
    suma = numeros_SO[i] + numeros_LAR[i] + numeros_IS[i]

    if ( ( (numeros_SO[i]%2 == 0) and (suma%2 == 0) ) or ( (numeros_SO[i]%2 == 1) and (suma%2 == 1)  ) ):
        puntos_SO+=1

    if ( ( (numeros_IS[i]%2 == 0) and (suma%2 == 0) ) or ( (numeros_IS[i]%2 == 1) and (suma%2 == 1)  ) ):
        puntos_IS+=1

    if ( ( (numeros_LAR[i]%2 == 0) and (suma%2 == 0) ) or ( (numeros_LAR[i]%2 == 1) and (suma%2 == 1)  ) ):
        puntos_LAR += 1

print(f'SO:{puntos_SO}, LAR:{puntos_LAR}, IS:{puntos_IS}')
