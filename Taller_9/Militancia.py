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

union = (pdc | pdd | pdi)
caso1 = 0
caso2 = 0
caso3 = 0
for elemento in union:

    if ( (elemento in pdc and elemento not in pdi and elemento not in pdd) or (elemento in pdd and elemento not in pdi and elemento not in pdc) or (elemento in pdi and elemento not in pdc and elemento not in pdd)  ):
        caso1 += 1
    
    elif ( (elemento in pdc and elemento in pdi and elemento not in pdd) or (elemento in pdd and elemento in pdi and elemento not in pdc) or (elemento in pdc and elemento in pdd and elemento not in pdi)):
        caso2 += 1
    
    elif(elemento in pdc and elemento in pdi and elemento in pdd):
        caso3 += 1
print(caso1, caso2, caso3)



# caso_1 = len((pdc) - (pdi | pdd)) + len((pdd) - (pdi | pdc)) + len((pdi) - (pdc | pdd))
# caso_2 = len( (pdc & pdi) - pdd ) + len( (pdd & pdi) - pdc ) +  len( (pdc & pdd) - pdi )
# caso_3 = len(pdc&pdi&pdd)
# print(caso_1, caso_2, caso_3)