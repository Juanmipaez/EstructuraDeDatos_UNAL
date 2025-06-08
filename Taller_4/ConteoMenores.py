casos = int(input())
ListaCasos = []

for numero_casos in range(casos):
    valores = list(map(int, input().split(" ")))
    valores.sort()

    if len(valores) != 0: 
        valor =  valores[0]
    else:
        print(0)

    repeticiones = 0
    Lista_indidivual_caso = []
    for index in range(len(valores)):
        if valores[index] == valor:
            repeticiones +=1
        else:
            Lista_indidivual_caso.append(repeticiones)
            repeticiones=1
            valor = valores[index]
    Lista_indidivual_caso.append(repeticiones)
    ListaCasos.append(Lista_indidivual_caso)

for lista in ListaCasos:
    print(*lista)
