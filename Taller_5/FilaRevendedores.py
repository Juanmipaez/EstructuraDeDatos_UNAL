from collections import deque

CantidadCompradores, BoletasDisponibles = map(int, input().split(" "))

BaseDatos = deque()
for caso in range(CantidadCompradores):
    BaseDatos.append(list(map(int, input().split(" "))))

BoletasCompradas = 0

conteo = 1
while len(BaseDatos) > 0 and BoletasDisponibles > BoletasCompradas:
    peek = BaseDatos[0][1]
    if (conteo) % 5 == 0:
        BoletasCompradas += BaseDatos[0][1]
        BaseDatos.popleft()
    else:
        BoletasCompradas += BaseDatos[0][1]
        if BoletasCompradas > BoletasDisponibles:
            ultimas = peek - (BoletasCompradas - BoletasDisponibles)
            print(BaseDatos[0][0], ultimas)
            break
        BaseDatos.append(BaseDatos[0])
        BaseDatos.popleft()
    conteo += 1
    if len(BaseDatos) == 0:
        print("quedaron boletas disponibles")
        break


