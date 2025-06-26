def primos_hasta(n):
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, n + 1, i):
                es_primo[j] = False

    primos = [i for i, primo in enumerate(es_primo) if primo]
    return primos

primos = primos_hasta(10000)
primos_set = set(primos)

cantidad_casos = int(input())

Orden = []
Parejas = {}

for _ in range(cantidad_casos):
    objetivo = int(input())
    Orden.append(str(objetivo))

    Parejas[f'{objetivo}'] = 0
    for primo1 in primos:
        if primo1 > objetivo//2:
            break
        complemento = objetivo-primo1
        if complemento in primos_set:
            Parejas[f'{objetivo}']+=1

for valores in Orden:
    print(Parejas[valores])