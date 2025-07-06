from collections import deque

class Node():
    def __init__(self):
        self.visited = False
        self.hops = None

def BFS(nodes, edges, start):
    nodes[start].visited = True
    nodes[start].hops = 0
    q = deque()
    q.append(start)

    conteo_por_dia = {}

    while q:
        a = q.popleft()
        for b in edges[a]:
            if not nodes[b].visited:
                nodes[b].visited = True
                nodes[b].hops = nodes[a].hops + 1
                dia = nodes[b].hops
                conteo_por_dia[dia] = conteo_por_dia.get(dia, 0) + 1
                q.append(b)

    if not conteo_por_dia:
        return 0, 0

    mejor_dia = -1
    maximo_radio = -1
    for dia in sorted(conteo_por_dia.keys()):
        if conteo_por_dia[dia] > maximo_radio:
            maximo_radio = conteo_por_dia[dia]
            mejor_dia = dia
            
    return mejor_dia, maximo_radio

def reset_nodes(nodos):
    for node in nodos.values():
        node.visited = False
        node.hops = None

tamaño_comunidad = int(input())

Grafo = []
for _ in range(tamaño_comunidad):
    datos_amigos = list(map(int, input().split()))
    if datos_amigos[0] != -1:
        Grafo.append(datos_amigos)
    else:
        Grafo.append([])

nodos = {k: Node() for k in range(tamaño_comunidad)}

casos = list(map(int, input().split(", ")))

for caso in casos:
    reset_nodes(nodos)
    dia, radio = BFS(nodos, Grafo, caso)
    if radio == 0:
        print(0)
    else:
        print(dia, radio)
