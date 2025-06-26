cantidad_palabras = int(input())

DiccionarioEwokCast = {}
for _ in range(cantidad_palabras):
    PalabraEwok, PalabraCast = input().split()
    DiccionarioEwokCast[PalabraEwok] = PalabraCast


Palabras = []
while True:
    palabra = input()
    if palabra == "#":
        break
    else:
        Palabras.append(palabra)

for palabra in Palabras:
    if palabra in DiccionarioEwokCast.keys():
        print(DiccionarioEwokCast[palabra])
    else:
        print("Entrada no encontrada")
