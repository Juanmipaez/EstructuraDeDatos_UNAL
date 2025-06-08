cantidad_de_casos = int(input())

for _ in range(cantidad_de_casos):
    tamaño_arreglo = int(input())
    saltos = list(map(int, input().split()))

    index_visitados = []
    i = 0
    saltos_realizados = 0

    while True:
        
        if i < 0 or i >= tamaño_arreglo or i in index_visitados:
            break

        index_visitados.append(i)
        i += saltos[i]
        saltos_realizados += 1

    print(saltos_realizados)
