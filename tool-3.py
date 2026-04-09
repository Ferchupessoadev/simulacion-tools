import random

lanzamientos = int(input("Ingrese cuántos lanzamientos de moneda se harán: "))

conteo = {"cara": 0, "cruz": 0}

for _ in range(lanzamientos):
    resultado = random.choice(["cara", "cruz"])
    conteo[resultado] += 1
    print(f"{resultado.capitalize()} ha aparecido {conteo[resultado]} veces.")

print("\nResultados finales:\n")

for lado, cantidad in conteo.items():
    print(f"{lado.capitalize()}: {cantidad} de {lanzamientos} lanzamientos")