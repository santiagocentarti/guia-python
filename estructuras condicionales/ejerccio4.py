palabra = input("Ingrese una palabra: ")

cantidadletras = len(palabra)

print("La palabra tiene", cantidadletras, "letras.")

ultima_letra = palabra
if ultima_letra in ['a', 'e', 'i', 'o', 'u']:
    termina_en_vocal = True
    print("La palabra termina en vocal.")
else:
    termina_en_vocal = False
    print("La palabra no termina en vocal.")

