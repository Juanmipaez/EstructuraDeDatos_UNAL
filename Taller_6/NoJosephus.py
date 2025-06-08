import heapq

NumeroCasos = int(input())
Resultados = []

for caso in range(NumeroCasos):
    NumeroJugadores, primoA, primoB = map(int,input().split(" "))

    Jugadores = list(range(1,NumeroJugadores+1))

    while len(Jugadores) > 1:
        for index, numero in enumerate(Jugadores):
            numero = (numero*primoA) % primoB
            Jugadores[index] = numero
        heapq.heapify(Jugadores)
        
        for _ in range(len(Jugadores)//2):
            heapq.heappop(Jugadores)
    Resultados.append(Jugadores[0])

for res in Resultados:
    print(res)    