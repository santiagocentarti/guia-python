import random

tiradamoneda = random.randint(0, 1)

resultadotirada = 'cara' if tiradamoneda == 0 else 'cruz'

apuesta = input("¿ cara o cruz? ").lower()

print("La moneda ha caído en:", resultadotirada)
if apuesta == resultadotirada:
        print("Ganaste")
else:
        print("Perdiste")