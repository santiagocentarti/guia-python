meses = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}

numeromes = int(input("Ingrese un número de mes: "))

if numeromes in meses:
    nombremes = meses[numeromes]
    print("El mes correspondiente al número", numeromes, "es:", nombremes)
else:
    print("El número de mes ingresado no es válido.")