# from collections import deque

# def BFS_Component(partida, llegada, grafo):
    
#     grafo[Letras[partida[0]]][partida[1]] = 1
#     q = deque()
#     q.append((partida[0], partida[1]))
#     contador=1
#     print(q)
#     while q:
#         x, y = q.popleft()
#         for dx, dy in [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2,-1)]:
#             mov_x = Letras2.index(x) + dx
#             mov_y = y + dy
#             if 0<=mov_x<8 and 0<=mov_y<8:
#                 if grafo[mov_x][mov_y] == 0:
#                     Grafo[mov_x][mov_y] = 1
#                     q.append((Letras2[mov_x], mov_y))
#                     print((Letras2[mov_x], mov_y+1))
#                     contador+=1
#     print(contador)

# # cantidad_casos = int(input())
# Letras2 = ["A","B","C","D","E","F","G","H"]
# Letras = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
# Visitados = [[0 for i in range(8)] for i in range(8)]
# Grafo = [[0 for i in range(8)] for i in range(8)]

# print(Grafo)

# BFS_Component(("A",7),0,Grafo)

# for _ in range(cantidad_casos):
#     inicio, final = input().split()
from collections import deque

LETRAS = "ABCDEFGH"

def knight_component(origen, llegada):
    n = 8
    visitado = [[0]*n for _ in range(n)]

    q = deque([origen])
    visitado[origen[0]][origen[1]] = 1
    cuenta = 0

    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]:
            nx, ny = x + dx, y + dy
            if (nx == llegada[0] and ny == llegada[1]) and 0 <= nx < n and 0 <= ny < n :
                cuenta+=1
                return cuenta
            elif 0 <= nx < n and 0 <= ny < n and visitado[nx][ny] == 0:
                visitado[nx][ny] = 1
                q.append((nx, ny))
                cuenta += 1

    return cuenta

casilla_humana = "B1"
casilla_llegada = "H8"

fila = int(casilla_humana[1]) - 1
col  = LETRAS.index(casilla_humana[0])

fila_llegada = int(casilla_llegada[1]) - 1
col_llegada  = LETRAS.index(casilla_llegada[0])

print(f"Casillas alcanzadas desde {casilla_humana}:", knight_component((fila, col),(fila_llegada, col_llegada)))
