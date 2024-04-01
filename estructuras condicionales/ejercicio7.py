import random

resultadodado = random.randint(1, 6)

apuesta = int(input("Apuesta al numero del dado (entre 1 y 6): "))

if apuesta == resultadodado:
        print("Ganaste el numero que salio fue: ", resultadodado)
else:
        print("Perdiste el numero que salio fue ", resultadodado)

