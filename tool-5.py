import random
from faker import Faker

fake = Faker()

clientes = []
tiempo_actual = 0
fin_anterior = 0

for i in range(10):
    llegada = tiempo_actual + random.randint(1, 3)
    tiempo_actual = llegada

    servicio = random.randint(2, 4)

    inicio = max(llegada, fin_anterior)

    fin = inicio + servicio

    espera = inicio - llegada

    fin_anterior = fin

    clientes.append({
        "cliente": fake.name(),
        "llegada": llegada,
        "servicio": servicio,
        "inicio": inicio,
        "fin": fin,
        "espera": espera
    })

print(f"{'Cliente':<20} {'Llegada':<8} {'Servicio':<9} {'Inicio':<8} {'Fin':<5} {'Espera':<7}")
for c in clientes:
    print(f"{c['cliente']:<20} {c['llegada']:<8} {c['servicio']:<9} {c['inicio']:<8} {c['fin']:<5} {c['espera']:<7}")

espera_total = sum(c["espera"] for c in clientes)
espera_promedio = espera_total / len(clientes)

hubo_cola = any(c["espera"] > 0 for c in clientes)

print("\nResultados:")
print(f"Espera promedio: {espera_promedio:.2f} minutos")
print(f"¿Hubo cola?: {'Sí' if hubo_cola else 'No'}")

