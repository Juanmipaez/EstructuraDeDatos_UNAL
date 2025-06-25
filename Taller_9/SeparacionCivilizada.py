libros_gustavo = set()
libros_fernando = set()

while True:
    datos = input().split()
    if datos[0] == "0":
        break
    else: 
        isbn, propietario = datos
        isbn = int(isbn)
    
        if (propietario == "F"):
            if isbn not in libros_gustavo:
                libros_fernando.add(isbn)
            else:
                if isbn%2 == 0:
                    libros_fernando.add(isbn)
                    libros_gustavo.remove(isbn)
        
        elif (propietario == "G"):
            if isbn not in libros_fernando:
                libros_gustavo.add(isbn)
            else:
                if isbn%2 == 1:
                    libros_gustavo.add(isbn)
                    libros_fernando.remove(isbn)

print(len(libros_fernando), len(libros_gustavo))