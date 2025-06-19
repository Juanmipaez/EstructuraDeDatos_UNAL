intersecciones = set()
intersecciones_parciales = set()

for _ in range(5):
    Cantidad_estudiantes = int(input())
    valores = set()
    for id in range(Cantidad_estudiantes):
        ids = input()
        valores.add(ids)
        intersecciones_parciales.add(ids)
    intersecciones = intersecciones & valores

print(intersecciones)