import random

total_paquetes = 50
perdidos = 0

print(f"{'Paquete':<10}{'Estado':<15}")

for i in range(1, total_paquetes + 1):
    if random.random() < 0.10:
        estado = "Perdido"
        perdidos += 1
    else:
        estado = "Enviado"
    
    print(f"{i:<10}{estado:<15}")

# Resultados
porcentaje_perdida = (perdidos / total_paquetes) * 100

print("\nResultados:")
print("1. Paquetes perdidos:", perdidos)
print("2. Porcentaje de pérdida real:", round(porcentaje_perdida, 2), "%")