numero_casos = int(input())
sumas = []

for caso in range(numero_casos):

    cantidades = list(map(int, input().split(" ")))
    denominaciones = list(map(int, input().split(" ")))
    lista_sumas = [0]*cantidades[0]

    for id in range(len(denominaciones)):
        lista_sumas[ (id % cantidades[0]) ] += denominaciones[id]
    sumas.append(max(lista_sumas) - min(lista_sumas))

for elemento in sumas:
    print(elemento)
