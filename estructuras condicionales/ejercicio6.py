frente = float(input("Ingrese la medida de frente del terreno: "))
fondo = float(input("Ingrese la medida de fondo del terreno: "))

if frente == fondo:
    print("El terreno es cuadrado.")
    forma = "cuadrado"
else:
    print("El terreno es rectangular.")
    forma = "rectangular"

superficie = frente * fondo

# Mostrar la superficie del terreno
print("La superficie del terreno", forma, "es:", superficie)