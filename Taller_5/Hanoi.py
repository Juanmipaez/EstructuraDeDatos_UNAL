from collections import deque

def procesa_caso(n, movimientos):
    A = deque(range(n, 0, -1)) 
    B = deque()
    C = deque()
    pilas = {'A': A, 'B': B, 'C': C}

    def cambio(mov):
        src, dst = mov.split()
        origen, destino = pilas[src], pilas[dst]

        if not origen:
            return False
        
        if destino and origen[-1] > destino[-1]:
            return False

        destino.append(origen.pop())
        return True

    for mov in movimientos:
        if mov == "X X":
            break
        if not cambio(mov):
            print("secuencia invalida")
            return

    if len(C) == n:
        print("soluciona la torre")
    else:
        print("no soluciona la torre")


C = int(input())
for _ in range(C):
    n = int(input())
    movimientos = []
    while True:
        linea = input().strip()
        movimientos.append(linea)
        if linea == "X X":
            break
    procesa_caso(n, movimientos)
