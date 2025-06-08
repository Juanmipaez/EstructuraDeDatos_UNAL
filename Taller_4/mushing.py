from bisect import bisect_left

cantidad_de_casos = int(input())
diferencias = []

for _ in range(cantidad_de_casos):
    
    pesos = list(map(int, input().split(", ")))
    pesos.sort()
    
    
    pref = []
    s = 0
    for i in pesos:
        s += i
        pref.append(s)
    total = s
    
    mitad = total / 2
    i = bisect_left(pref, mitad)
    
    candidatos = []
    if i < len(pref):
        candidatos.append(abs(total - 2*pref[i]))
    if i > 0:
        candidatos.append(abs(total - 2*pref[i-1]))
    
    diferencias.append(min(candidatos))

for d in diferencias:
    print(d)

