Lista_maximos = []

while True:
    Id_datos = input()
    if Id_datos == "0 0":
        break

    Id_datos = Id_datos.split(" ")
    Id = Id_datos[0]
    maximo = int(Id_datos[1])

    if any(Id == fanatico[0] for fanatico in Lista_maximos):
        continue

    if len(Lista_maximos) == 0:
        Lista_maximos.append((Id,maximo))

    elif maximo > len(Lista_maximos):
        Lista_maximos.append((Id,maximo))

        while any(len(Lista_maximos) > fanatico[1] for fanatico in Lista_maximos):
            for i, (id_fila, max_fila) in enumerate(Lista_maximos):
                if len(Lista_maximos) > max_fila:
                    Lista_maximos.pop(i)
                    break

print(len(Lista_maximos))
