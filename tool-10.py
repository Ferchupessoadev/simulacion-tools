import random

periodos = 10
infectados = 2

print(f"{'Periodo':<10}{'Nuevos':<10}{'Total':<10}")

for t in range(1, periodos + 1):
    nuevos = 0
    
    for _ in range(infectados):
        if random.random() < 0.5:
            nuevos += 1
    
    infectados += nuevos
    
    print(f"{t:<10}{nuevos:<10}{infectados:<10}")

print("\nResultados:")
print("1. Infectados al final:", infectados)

print("2. La propagación crece de forma probabilística,")
print("   generalmente similar a un crecimiento exponencial al inicio,")
print("   pero con variaciones aleatorias en cada período.")