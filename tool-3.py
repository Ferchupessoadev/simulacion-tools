import random as r

l = int(input("ingrese cuantos lanzamientos de moneda se harán: "))

lanzamientos = 0
cruz = 0
cara = 0
while (lanzamientos < l):
    sel = r.randint(1, 2)

    if (sel == 1):
        cara = cara + 1
        print(f"cara ha aparecido {cara} veces.")
    else:
        cruz = cruz + 1
        print(f"Cruz ha aparecido {cruz} veces.")
    
    lanzamientos += 1

print(f"la frecuencia con la que aparece cara es {cara} de cada {lanzamientos} lanzamientos.")
print(f"la frecuencia con la que aparece cruz es {cruz} de cada {lanzamientos} lanzamientos.")