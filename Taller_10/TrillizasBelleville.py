CantidadNumeros, Suma = input().split()
CantidadNumeros = int(CantidadNumeros)
Suma = int(Suma)

Numeros = []

for _ in range(CantidadNumeros):
    Numeros.append(int(input()))

NumeroEnConjunto = set(Numeros)

Tripletas = set()
for i in range(CantidadNumeros-1):
    for j in range(i+1, CantidadNumeros):
        Num1 = Numeros[i]
        Num2 = Numeros[j]
        Complemento = Suma-Num1-Num2
        Tripleta = [Num1, Num2, Complemento]
        if (Complemento) in NumeroEnConjunto and Complemento!=Num1 and Complemento!=Num2:
            Tripleta = tuple(sorted(Tripleta))
            Tripletas.add(Tripleta)

Tripletas = list(Tripletas)
Tripletas.sort()

if Tripletas:
    for elemento in Tripletas:
        print(*elemento)
else:
    print("No hay trillizas")