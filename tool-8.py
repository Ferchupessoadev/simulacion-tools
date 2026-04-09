import random

# Configuración
clientes = 15
tiempo_llegada = 0
fin_atencion = 0

tiempos_espera = []
queue = 0
queue_max = 0

print(f"{'Cliente':<10}{'Llega':<10}{'Inicio':<10}{'Fin':<10}{'Espera':<10}{'Cola':<10}")

for i in range(1, clientes + 1):
    # Tiempo entre llegadas (2 a 5 minutos)
    if i == 1:
        tiempo_llegada = 0
    else:
        tiempo_llegada += random.randint(2, 5)
    
    # Tiempo de operación (1 a 4 minutos)
    tiempo_operacion = random.randint(1, 4)
    
    # Inicio de atención
    inicio_atencion = max(tiempo_llegada, fin_atencion)
    
    # Tiempo de espera
    espera = inicio_atencion - tiempo_llegada
    tiempos_espera.append(espera)
    
    # Fin de atención
    fin_atencion = inicio_atencion + tiempo_operacion
    
    # Calcular cola (clientes esperando)
    if espera > 0:
        queue += 1
    else:
        queue = 0
    
    queue_max = max(queue_max, queue)
    
    print(f"{i:<10}{tiempo_llegada:<10}{inicio_atencion:<10}{fin_atencion:<10}{espera:<10}{queue:<10}")

# Resultados
promedio_espera = sum(tiempos_espera) / clientes

print("\nResultados:")
print("1. Tiempo promedio de espera:", round(promedio_espera, 2), "minutos")
print("2. Mayor cola:", queue_max)