casos_de_prueba = int(input())

palabras = []
for i in range(casos_de_prueba):
    palabra = input().replace(" ", "")
    palabras.append(palabra)

for palabra in palabras:
    retroceder = list(palabra[::-1])
    copia_palabra = list(retroceder.copy())
    for i in range(0,len(copia_palabra)-1,2):
        retroceder[i] = copia_palabra[i+1]
        retroceder[i+1] = copia_palabra[i]
    print("".join(retroceder))
