import heapq

cantidad_casos = int(input())

resultados = []

for caso in range(cantidad_casos):
    datos = list(map(int,input().split(" ")[:-1]))
    heapq.heapify(datos)

    while len(datos) > 2:
        menor = heapq.heappop(datos)
        segundo_menor = heapq.heappop(datos)
        suma = menor + segundo_menor

        heapq.heappush(datos, suma)
    resultados.append(datos)

for res in resultados:
    print(f'{res[0]} {res[1]}')