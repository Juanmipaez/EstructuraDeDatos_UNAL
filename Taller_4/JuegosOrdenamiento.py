cantidad_casos = int(input())

cantidad_cambios = []
for _ in range(cantidad_casos):
    documentos = list(map(int, input().split(" ")))
    documentos_ordenados = sorted(documentos)

    if len(documentos) == 1:
        print(1)
    
    cambios = 0
    while True:
        for i in range(len(documentos) - 1):
            if documentos[i] > documentos[i+1]:
                documentos[i], documentos[i+1] = documentos[i+1], documentos[i]
                cambios+=1
        if documentos == documentos_ordenados:
            cantidad_cambios.append(cambios)
            break

for j in cantidad_cambios:
    print(j)
