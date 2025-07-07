from collections import deque

def BFS_Component(i, j):
    
    visitados[i][j] = 1
    q = deque()
    q.append((i, j))
    nodos_visitados = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            mov_x = x + dx
            mov_y = y + dy
            if 0<=mov_x<A and 0<=mov_y<B:
                if Grafo[mov_x][mov_y] == "X" and visitados[mov_x][mov_y] == 0:
                    visitados[mov_x][mov_y] = 1
                    nodos_visitados+=1
                    q.append((mov_x, mov_y))
    return nodos_visitados

cantidad_casos = int(input())

Resultados = []

for _ in range(cantidad_casos):
    
    Grafo = []
    A, B = map(int, input().split())
    
    for _ in range(A):
        palabra = input()
        Grafo.append(palabra)
    
    visitados = [[0 for _ in range(B)] for _ in range(A)]
    
    area = 0
    for i in range(A):
        for j in range(B):
            if Grafo[i][j] == "X" and visitados[i][j] == 0:
                area_parcial = BFS_Component(i,j)
                if area_parcial>area:
                    area = area_parcial
    
    Resultados.append(area)

for _ in Resultados:
    print(_)