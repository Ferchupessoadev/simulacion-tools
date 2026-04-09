import random

segundos = 20
queue = 0
queue_max = 0

print(f"{'Tiempo':<10}{'Llegan':<10}{'Cola':<10}")

for t in range(1, segundos + 1):
    llegan = random.randint(0, 2)
    
    queue += llegan
    
    if queue > 0:
        queue -= 1
    
    if queue > queue_max:
        queue_max = queue
    
    print(f"{t:<10}{llegan:<10}{queue:<10}")

print("\nResultados:")
print("1. Cola máxima:", queue_max)

if queue == 0:
    print("2. El router logró procesar todos los paquetes.")
else:
    print("2. El router NO logró procesar todos los paquetes.")