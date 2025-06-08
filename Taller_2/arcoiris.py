tamaño_arreglo = int(input())

palabra = tuple(input().split(", "))

palabra_completa = ()

for i in range((tamaño_arreglo + 1) // 2):
    if i == tamaño_arreglo - 1 - i:
        palabra_completa += (palabra[i],)
    else:
        palabra_completa += (palabra[i], palabra[tamaño_arreglo - 1 - i])

print("".join(palabra_completa))

