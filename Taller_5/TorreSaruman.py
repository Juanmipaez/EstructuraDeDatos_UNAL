from collections import deque

cantidad_casos = int(input())
pilas = []

for caso in range(cantidad_casos):
    datos = deque(map(int, input().split(" ")))
    pilas.append(datos)

for pila in pilas:
    if len(pila) == 0:
            print("0 0")
            break
    while True:
        if len(pila) == 1:
            print(1, pila[0])
            break
        else:
            top = pila.pop()
            subtop = pila.pop()
            if (top+subtop) % 2 == 0:
                nuevo_top = (top+subtop)//2
                pila.append(nuevo_top)
            elif (top+subtop) % 2 != 0:
                pila.append(subtop)
                pila.append(top)
                print(len(pila), pila[-1])
                break