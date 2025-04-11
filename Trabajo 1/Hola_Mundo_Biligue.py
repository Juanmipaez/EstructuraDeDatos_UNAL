mensajes = ["Hola mundo", "Hello world"]
numero = int(input())
for i in range(numero):
    print(mensajes[i % 2])

