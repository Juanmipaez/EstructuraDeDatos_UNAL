Resultados = []

numero_de_casos = int(input())

for _ in range(numero_de_casos):

    cantidad_de_parejas = int(input())
    familias = []
    persona_a_familia = {}              

    for _ in range(cantidad_de_parejas):
        persona1, persona2 = input().split()

        fam1 = persona_a_familia.get(persona1)
        fam2 = persona_a_familia.get(persona2)

        if fam1 is not None and fam2 is not None:
            if fam1 != fam2:
                # Fusionar las dos familias
                if len(familias[fam2]) > len(familias[fam1]):
                    fam1, fam2 = fam2, fam1 

                familias[fam1].update(familias[fam2])

                for persona in familias[fam2]:
                    persona_a_familia[persona] = fam1

                familias[fam2] = set()

        elif fam1 is not None:
            familias[fam1].add(persona2)
            persona_a_familia[persona2] = fam1

        elif fam2 is not None:
            familias[fam2].add(persona1)
            persona_a_familia[persona1] = fam2

        else:
            nueva_familia = {persona1, persona2}
            familias.append(nueva_familia)
            indice = len(familias) - 1
            persona_a_familia[persona1] = indice
            persona_a_familia[persona2] = indice

    familias = [grupo for grupo in familias if grupo]

    cantidad_total = len(familias)
    tamaño_maximo = max(len(grupo) for grupo in familias)

    Resultados.append((cantidad_total, tamaño_maximo))

for i in Resultados:
    print(*i)
