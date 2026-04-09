a = int(input("Ingrese cuanto dinero depositará: "))
b = int(input("Ingrese el porcentaje de interés: "))
c = int(input("Ingrese la cantidad de ciclos: "))
d = 1
while (d < c):
    a = a * b / 100 + a
    print(f"en el ciclo {d}, el dinero es {a}")
    d += 1