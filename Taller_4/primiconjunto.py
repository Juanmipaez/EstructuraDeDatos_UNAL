from bisect import bisect_left
casos = int(input())
Resultados = []

for _ in range(casos):
    longitud_arreglo, numero = map(int, input().split())
    arreglo = list(set(map(int, input().split())))
    arreglo.sort()

    divisores = 0
    divisores_en_lista = 0

    for index in range(1, (numero // 2) + 1):
        if numero % index == 0:
            divisores += 1
            if index in arreglo:
                divisores_en_lista += 1

    divisores+=1
    idx_primo = bisect_left(arreglo, numero)
    if idx_primo < len(arreglo) and arreglo[idx_primo] == numero:
        divisores_en_lista+=1

    if divisores == divisores_en_lista:
        Resultados.append("Es PrimiConjunto")
    else:
        Resultados.append("No es PrimiConjunto")

print("\n".join(Resultados))