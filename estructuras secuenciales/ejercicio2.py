p1 = float(input("Ingrese la inversión de la primera persona: "))
p2 = float(input("Ingrese la inversión de la segunda persona: "))
p3 = float(input("Ingrese la inversión de la tercera persona: "))

inversion = p1 + p2 + p3

porcentajep1 = (p1 / inversion) * 100
porcentajep2 = (p2 / inversion) * 100
porcentajep3 = (p3 / inversion) * 100
    
print("Porcentaje de inversión de la primera persona:", porcentajep1, "%")
print("Porcentaje de inversión de la segunda persona:", porcentajep2, "%")
print("Porcentaje de inversión de la tercera persona:", porcentajep3, "%")
