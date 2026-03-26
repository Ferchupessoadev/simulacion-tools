import random
lanzamientos = int(input("Ingrese cuantos lanzamientos de dado hará: "))
ciclos = 0
a = 0
aa = "uno"
bb = "dos"
cc = "tres"
dd = "cuatro"
ee = "cinco"
ff = "seis"
b = 0
c = 0
d = 0
e = 0
f = 0
while (ciclos < lanzamientos):
    random_number = random.randint(1,6)
    if(random_number == 1):
        a = a + 1
        print(f"el uno ha aparecido {a} veces.")
    if(random_number == 2):
        b = b + 1
        print(f"el dos ha aparecido {b} veces.")
    if(random_number == 3):
        c = c + 1
        print(f"el tres ha aparecido {c} veces.")
    if(random_number == 4):
        d =d + 1
        print(f"el cuatro ha aparecido {d} veces.")
    if(random_number == 5):
        e = e + 1
        print(f"el cinco ha aparecido {e} veces.")
    if(random_number == 6):
        f = f + 1
        print(f"el seis ha aparecido {f} veces.")
    ciclos += 1
    may=max(a,b,c,d,e,f)
if (a==may):
    print(f"El lado que más veces ha salido fué el {aa}")
if (b==may):
    print(f"El lado que más veces ha salido fué el {bb}")
if (c==may):
    print(f"El lado que más veces ha salido fué el {cc}")
if (d==may):
    print(f"El lado que más veces ha salido fué el {dd}")
if (e==may):
    print(f"El lado que más veces ha salido fué el {ee}")
if (f==may):
    print(f"El lado que más veces ha salido fué el {ff}")

print("promedio de veces que salieron cada número del dado\n")

print(f"1: {a} veces en {ciclos} tiradas.")
print(f"2: {b} veces en {ciclos} tiradas.")
print(f"3: {c} veces en {ciclos} tiradas.")
print(f"4: {d} veces en {ciclos} tiradas.")
print(f"5: {e} veces en {ciclos} tiradas.")
print(f"6: {f} veces en {ciclos} tiradas.")