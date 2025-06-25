CantidadPoblacionInicial = int(input())
Lista_Inicial = set(list(range(1,CantidadPoblacionInicial+1)))
Resultados = []

while True:
    datos = input().split()
    if datos[0] == "#":
        break
    
    elif ( (datos[0] == "new") and (int(datos[1]) in Lista_Inicial) and (int(datos[2]) in Lista_Inicial) ):
        suma = int(datos[1]) + int(datos[2])
        while suma in Lista_Inicial:
            suma+=1
        Lista_Inicial.add(suma)

    elif datos[0] == "search":
        if int(datos[1]) in Lista_Inicial:
            Resultados.append("existe")
        else:
            Resultados.append("no existe")

for _ in Resultados:
    print(_)