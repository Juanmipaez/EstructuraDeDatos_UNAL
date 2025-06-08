import heapq
numero_casos = int(input())

sumas = []

for caso in range(numero_casos):
    
    cantidad_numeros = int(input())
    X = ''
    Y = ''
    numeros = input().split(" ")
    heapq.heapify(numeros)

    for index in range(cantidad_numeros):

        if index % 2 == 0:
            X += heapq.heappop(numeros)
        else:
            Y += heapq.heappop(numeros)
    
    sumas.append(int(X)+int(Y))

for sum in sumas:
    print(sum)