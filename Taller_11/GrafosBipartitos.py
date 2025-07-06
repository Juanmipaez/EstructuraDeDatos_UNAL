from collections import deque

def BFS(edges, colores, start):
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        a-=1
        for b in edges[a]:
            b-=1
            if colores[b] == -1:
                colores[b] = 1 - colores[a]
                q.append(b+1)
            elif colores[b] == colores[a]:
                return False
    return True

cantidad_casos = int(input())

Resultados = []

for caso in range(cantidad_casos):

    cantidad_nodos, cantidad_aristas = map(int, input().split())

    Grafo = [[]  for i in range(cantidad_nodos)]

    for aristas in range(cantidad_aristas):
        nodo1, nodo2 = map(int, input().split(", "))

        Grafo[nodo1-1].append(nodo2)
        Grafo[nodo2-1].append(nodo1)
    
    nodos = [nodo for nodo in range(1, cantidad_nodos+1)]
    
    colores = [-1] * (cantidad_nodos)

    es_bipartito = True
    for nodo in nodos:
        if colores[nodo-1] == -1:
            if not BFS(Grafo, colores, nodo):
                es_bipartito = False
                break
    
    Resultados.append("bipartito" if es_bipartito else "no bipartito")

for res in Resultados:
    print(res)
