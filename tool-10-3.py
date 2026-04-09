import random

def simular_propagation(periodos=10, infectados_iniciales=2):
    periodos = periodos
    infectados = infectados_iniciales

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
    return infectados

print("Primera simulación:")
first_simulation = simular_propagation()
print("\nSegunda simulación:")
second_simulation = simular_propagation()
print("\nTercera simulación:")
third_simulation = simular_propagation()

print("\nComparación de resultados:")
print(f"Simulación 1: Infectados al final: {first_simulation}")
print(f"Simulación 2: Infectados al final: {second_simulation}")
print(f"Simulación 3: Infectados al final: {third_simulation}")

print("\nConclusión:")

minimum_infectados = min(first_simulation, second_simulation, third_simulation)
maximum_infectados = max(first_simulation, second_simulation, third_simulation)
diferencia = maximum_infectados - minimum_infectados
print(f"Variación\n")
print(f"Entre las tres simulaciones, el número de infectados al final varió entre {minimum_infectados} y {maximum_infectados}, con una diferencia de {diferencia}.")

print(f"Diferencia entre simulaciones\n")
print(f"La mayor diferencia fue de {diferencia} infectados entre las simulaciones.")