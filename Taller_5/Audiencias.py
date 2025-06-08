from collections import deque
cantidad_casos = int(input())

tiempos = []

for caso in range(cantidad_casos):
    cantidad_jugadores, posicion_elfo = map(int, input().split(" "))
    peticiones = map(int, input().split(" "))
    fila = deque(peticiones)

    posicion_elfo -= 1
    tiempo = 0
    while True:
        tiempo += 5
        numero = fila.popleft()
        if posicion_elfo != 0:
            if numero > 1:
                fila.append(numero-1)
            posicion_elfo-=1

        elif (posicion_elfo==0 and numero == 1):
            tiempos.append(tiempo)
            break

        elif (posicion_elfo==0 and numero != 1):
            fila.append(numero-1)
            posicion_elfo = len(fila) - 1

for i in tiempos:
    print(i)