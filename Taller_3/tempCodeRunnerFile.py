Maximos_por_jugador = []

while True:
    fanaticos = input()
    if fanaticos == "0 0":
        break
    
    fanaticos.split(" ")
    if len(Maximos_por_jugador) < int(fanaticos[1]):
        Maximos_por_jugador.append((fanaticos[0]),(fanaticos[1]))
    print(Maximos_por_jugador)