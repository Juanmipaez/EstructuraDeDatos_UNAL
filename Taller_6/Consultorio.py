import heapq

fila = []
while True:
    dato = input()
    if dato.isdigit():
        heapq.heappush(fila,int(dato))
    elif dato == "sig":
        if fila:
            ultimo = heapq.heappop(fila)
        else:
            continue
    elif dato == "end":
        print(ultimo)
        break
