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
    while q:
        a = q.popleft()
        for b in edges[a]:
            if nodes[b].visited == False and b != start:
                nodes[b].visited = True
                nodes[b].hops = nodes[a].hops + 1
                q.append(b)

numero_casos = int(input())

Resultados = []

for _ in range(numero_casos):
    numero_invitados, numero_parejas = map(int, input().split(","))
    Grafos = {i: set() for i in range(numero_invitados)}

    nodos = {}
    for k in Grafos.keys():
        nodos[k] = Node()

    for parejas in range(numero_parejas):
        pareja1, pareja2 = map(int, input().split())
        Grafos[pareja1].add(pareja2), Grafos[pareja2].add(pareja1)
    BFS(nodos, Grafos, 0)

    ListaParcial = []
    for i in range(1,numero_invitados):
        if nodos[i].hops is not None:
            ListaParcial.append((i,nodos[i].hops))
        else:
            ListaParcial.append((i,"INF"))
    Resultados.append(ListaParcial)

for j in range(numero_casos-1):
    print(f'fiesta {j+1}: ')
    for listaUnitaria in Resultados[j]:
        print(*listaUnitaria)
    print("")

print(f'fiesta {numero_casos}: ')
for listaUnitaria in Resultados[-1]:
    print(*listaUnitaria)