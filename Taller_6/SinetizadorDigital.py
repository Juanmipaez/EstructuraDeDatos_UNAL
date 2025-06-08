import heapq

DuracionCancion = int(input())
CantidadTonos = int(input())

Apariciones = []

for tonos in range(CantidadTonos):
    IdTono, PrimeraAparicion, frecuencia = map(int, input().split(" "))
    Lista = [i for i in range(PrimeraAparicion, DuracionCancion+1, frecuencia)]
    Apariciones += Lista

heapq.heapify(Apariciones)

for _ in range(len(Apariciones)):
    print(heapq.heappop(Apariciones))