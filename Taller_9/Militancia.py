pdc = set()
pdi = set()
pdd = set()

while True:
    datos = input().split()
    if datos[0] == "#":
        break
    else:
        votante, partido = datos
        if partido == "pdc":
            pdc.add(votante)
        elif partido == "pdi":
            pdi.add(votante)
        elif partido == "pdd":
            pdd.add(votante)

caso_1 = len((pdc) - (pdi | pdd)) + len((pdd) - (pdi | pdc)) + len((pdi) - (pdc | pdd))
caso_2 = len( (pdc & pdi) - pdd ) + len( (pdd & pdi) - pdc ) +  len( (pdc & pdd) - pdi )
caso_3 = len(pdc&pdi&pdd)
print(caso_1, caso_2, caso_3)