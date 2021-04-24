def readint(prompt, min, max):
    while True:
        try:
            n=int(input(prompt ))
            assert n<-10 or n<10
            return n
        except ValueError:
            print("Error: entrada incorrecta ")
        except:
             print("El valor no esta dentro del rango permitido ")

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)
