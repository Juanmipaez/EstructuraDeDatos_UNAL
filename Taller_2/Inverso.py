cantidad_de_numeros = int(input())
numeros_usuario = tuple(input().split(" "))

sumatoria_parcial = int(numeros_usuario[-1])
index = -2

if ( len(numeros_usuario) == cantidad_de_numeros ):
    for i in range(cantidad_de_numeros - 1 ):
        sumatoria_parcial += int(numeros_usuario[index])
        index -= 1
        print(sumatoria_parcial)