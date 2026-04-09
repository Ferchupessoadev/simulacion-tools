import random

lanzamientos = int(input("Ingrese cuántos lanzamientos de dado hará: "))

# Lista para contar apariciones (índice 0 = cara 1, etc.)
conteo = [0] * 6

# Simulación
for i in range(lanzamientos):
    numero = random.randint(1, 6)
    conteo[numero - 1] += 1
    print(f"El {numero} ha aparecido {conteo[numero - 1]} veces.")

# Resultado máximo
maximo = max(conteo)

print("\nEl/los lado(s) que más salieron:")

nombres = ["uno", "dos", "tres", "cuatro", "cinco", "seis"]

for i in range(6):
    if conteo[i] == maximo:
        print(f"El lado {nombres[i]}")

# Resumen final
print("\nResumen de resultados:\n")

for i in range(6):
    print(f"{i+1}: {conteo[i]} veces en {lanzamientos} tiradas.")