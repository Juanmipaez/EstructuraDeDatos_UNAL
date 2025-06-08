from collections import deque

numero_casos = int(input())

expresiones = []
for i in range(numero_casos):
    expresion = input().split(" ")
    expresion.pop(-1)
    expresiones.append(expresion)

for expresion in expresiones:
    stack = deque()
    correcta = True
    pares_sf = 0

    for simbolo in expresion:
        if simbolo in ("(", "{", "["):
            stack.append(simbolo)
        elif simbolo in (")", "}", "]"):
            if not stack:
                correcta = False
                break
            tope = stack.pop()
            if (tope == "(" and simbolo != ")") or \
               (tope == "{" and simbolo != "}") or \
               (tope == "[" and simbolo != "]"):
                correcta = False
                break
            pares_sf += 1

    if correcta and not stack and pares_sf == (len(expresion) // 2):
        print("correcta")
    else:
        print("incorrecta")