valores_felipe = set()
valores_vanesa = set()

while True:
    datos = input().split()
    if datos[0] == "#":
        break
    elif datos[0] == "F":
        valores_felipe.add(int(datos[1]))
    elif datos[0] == "V":
        valores_vanesa.add(int(datos[1]))

diferencia_simetrica = valores_felipe | valores_vanesa
print(len(valores_felipe), len(valores_vanesa), len(diferencia_simetrica))