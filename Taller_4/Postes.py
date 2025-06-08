from bisect import bisect_left
distancias = []

tamaño_autopista = int(input())
codigos = list(map(int, input().split(" ")))
codigos.sort()
cantidad_parejas = int(input())

for _ in range(cantidad_parejas):
    poste1, poste2 = map(int, input().split(" "))
    idx1 = bisect_left(codigos, poste1)
    idx2 = bisect_left(codigos, poste2)

    distancia = abs(idx2-idx1)
    distancias.append(distancia)

for distancia in distancias:
    print(f'{distancia} kms')
