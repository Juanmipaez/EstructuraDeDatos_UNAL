palabras = []
palabras_set = set()

while True:
    palabra = input()
    if palabra == "#":
        break
    else:
        palabras.append(palabra)
        palabras_set.add(palabra)

Composicion = []
for palabra in palabras:
    for slice in range(1, len(palabra)):
        prefijo = palabra[:slice]
        sufijo = palabra[slice:]
        if prefijo in palabras_set and sufijo in palabras_set:
            Composicion.append((palabra,prefijo,sufijo))
Composicion.sort()

if Composicion:
    for PalComp in Composicion:
        print(f'{PalComp[0]} = {PalComp[1]} + {PalComp[2]}')
