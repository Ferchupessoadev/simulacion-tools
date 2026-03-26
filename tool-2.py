a = int(input("Ingrese cuanto dinero depositará: "))
b = int(input("Ingrese el porcentaje de interés: "))
c = int(input("Ingrese la cantidad de ciclos: "))
d = 1
while (d<c):
    a = a*b/100+a
    d=d+1
    print("en este ciclo, el dinero es "+str(a))