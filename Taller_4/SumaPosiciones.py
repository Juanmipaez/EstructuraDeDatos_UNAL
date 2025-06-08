from bisect import bisect_left
tamaño_arreglo = int(input())
arreglo_numeros = list(set(map(int, input().split(" "))))
arreglo_numeros.sort()

cantidad_valores_a_verificar = int(input())
valores_a_buscar = list(map(int, input().split(" ")))
valores_a_buscar.sort()

suma = 0

for elemento in valores_a_buscar:
    idx = bisect_left(arreglo_numeros, elemento)
    if idx < len(arreglo_numeros) and arreglo_numeros[idx] == elemento:
        suma+=idx+1

print(suma)