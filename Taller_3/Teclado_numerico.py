secciones = []
numero = []

while True:

    input_user = input()
    if input_user == "end":
        union = ("").join(numero)
        break

    if input_user.isdigit():
        numero.append(input_user)

    elif (input_user == "C"):
        if len(numero)!=0:
            numero.pop(-1)
        
    elif (input_user[0] == "M"):
        input_user = input_user.split(" ")
        i = int(input_user[1])
        j = int(input_user[2])
        long1 = len(numero[i-1:j])
        long2 = 1+j-i

        if ( long1 == long2 ):    
            seccion = numero[i-1:j]
            secciones.append(("").join(seccion))
        else:
            continue

    elif (input_user[0] == "D"):
        input_user = input_user.split(" ")
        i = int(input_user[1])

        if ( i <= len(numero) ):    
            numero = numero[0:len(numero)-i]
        else:
            continue

for i in secciones:
    print(i)
