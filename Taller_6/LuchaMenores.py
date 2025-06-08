import heapq

A = []
B = [] 
C = []


puntos_a = 0
puntos_b = 0
puntos_c = 0


while True:
    datos = input().split(" ")
    if datos[0] == "A":
        heapq.heappush(A,int(datos[1]))
    elif datos[0] == "B":
        heapq.heappush(B,int(datos[1]))
    elif datos[0] == "C":
        heapq.heappush(C,int(datos[1]))

    
    if datos[0] == "menores":
        menores_caso = []
        if A:
            heapq.heappush(menores_caso,A[0])
        if  B:
            heapq.heappush(menores_caso,B[0])
        if C:
            heapq.heappush(menores_caso,C[0])
        
        if A:
            if A[0] == menores_caso[0]:
                puntos_a+=1
            heapq.heappop(A)
        if B:
            if B[0] == menores_caso[0]:
                puntos_b+=1
            heapq.heappop(B)
        if C:
            if C[0] == menores_caso[0]:
                puntos_c+=1
            heapq.heappop(C)
        
    if " ".join(datos) == "fin del juego":
        print(f'Equipo A: {puntos_a}')
        print(f'Equipo B: {puntos_b}')
        print(f'Equipo C: {puntos_c}')
        break