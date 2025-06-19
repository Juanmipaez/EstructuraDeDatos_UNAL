poblacion_vivos = set()
poblacion_muertos = set()

while True:
    datos = input().split()
    if datos[0] == "E":
        break

    elif (datos[0] == "B") and (datos[0] not in poblacion_muertos):
        poblacion_vivos.add(datos[1])

    elif (datos[0] == "D") and (datos[1] in poblacion_vivos):
        poblacion_vivos.remove(datos[1])
        poblacion_muertos.add(datos[1])
    
    elif (datos[0] == "R") and (datos[1] in poblacion_muertos):
        poblacion_vivos.add(datos[1])
        poblacion_muertos.remove(datos[1])
    
print(len(poblacion_vivos))