poblacion_vivos = set()
poblacion_muertos = set()
poblacion_resucitados = set()

while True:
    datos = input().split()
    if datos[0] == "E":
        break

    elif (datos[0] == "B") and (datos[1] not in poblacion_muertos) and (datos[1] not in poblacion_resucitados):
        poblacion_vivos.add(datos[1])

    elif (datos[0] == "D") and (datos[1] in poblacion_vivos):
        poblacion_vivos.remove(datos[1])
        poblacion_muertos.add(datos[1])
        if datos[1] in poblacion_resucitados:
            poblacion_resucitados.remove(datos[1])
    
    elif (datos[0] == "R") and (datos[1] in poblacion_muertos):
        poblacion_vivos.add(datos[1])
        poblacion_resucitados.add(datos[1])
        poblacion_muertos.remove(datos[1])
    
print(len(poblacion_vivos))