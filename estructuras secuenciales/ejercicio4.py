lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

perimetro = lado1 + lado2 + lado3

sp = perimetro / 2

area = (sp * (sp - lado1) * (sp - lado2) * (sp - lado3))**0.5

print("El perímetro del triángulo es:", perimetro)
print("El área del triángulo es:", area)