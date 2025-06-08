numero_casos = int(input())
posiciones_ganadoras = []

for _ in range(numero_casos):
    datos = input().split(" ")
    numero_estudiantes = int(datos[0])
    conteo_K = int(datos[1])

    Estudiantes = [i + 1 for i in range(numero_estudiantes)]

    posicion = 0
    while len(Estudiantes) > 1:
        posicion = (posicion + conteo_K - 1) % len(Estudiantes)
        eliminado = Estudiantes.pop(posicion)
        conteo_K = eliminado % len(Estudiantes) if len(Estudiantes) > 0 else 1
        if conteo_K == 0:
            conteo_K = 1

    posiciones_ganadoras.append(Estudiantes[0])

for ganador in posiciones_ganadoras:
    print(ganador)