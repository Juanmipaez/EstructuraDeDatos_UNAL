Premio_M = int(input())

Balotas_Compradas = {}
BalotasGanadoras = set()
Premios = []

while True:
    datos = input().split()
    if datos[0] == "end":
        break
    else:
        formato, balota = datos[0], datos[1]

                
        if formato == "winner":
            BalotasGanadoras.add(balota)

        if formato == "sms":
            if balota not in Balotas_Compradas:
                Balotas_Compradas[balota] = 1
            else:
                Balotas_Compradas[balota] += 1
            
            if balota in BalotasGanadoras:
                premio = Premio_M//(len(BalotasGanadoras)*int(Balotas_Compradas[balota]))

                Premios.append((balota, premio))

if Premios:
    for ganadores in Premios:
        print(ganadores[0], ganadores[1])
else:
    print("0")