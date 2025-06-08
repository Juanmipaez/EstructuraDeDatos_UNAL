from collections import deque

DatosDelCaso = deque()

while True:
    datos = input().split(" ")

    if len(datos) == 1 and datos[0] == "termina":
        if len(DatosDelCaso) > 0:
            print(f'cabeza {DatosDelCaso[0]} cola {DatosDelCaso[-1]}')
        else:
            print('uroboro vacio')
        break

    elif len(datos) == 2:
        DatosDelCaso.append(int(datos[1]))

    elif (datos[0] == "engulle") and (len(DatosDelCaso) > 0):
        if DatosDelCaso[0] > DatosDelCaso[-1]:
            DatosDelCaso.pop()
        else:
            DatosDelCaso.popleft()

    elif datos == "engulle" and len(DatosDelCaso[0]) == 0:
        continue
    