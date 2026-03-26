import random as r
# Una tienda comienza con 20 productos en stock.
# Cada día:
#  se venden 0–5 productos
#  si el stock baja a 5, se reponen 15 productos
# Simular 15 días.
# Preguntas
# 1. ¿Cuántas veces se repuso el inventario?
# 2. ¿Hubo días sin stock?
stock = 20
restock = 0
sinstock = 0
dia = 0
ciclos = int(input("Dias que durará la simulación: "))
while(dia<ciclos):
    ventadia = r.randint(0,5)
    stock = stock-ventadia
    if(stock<5):
        stock += 15
        restock +=1
    if(stock<=0):
        sinstock +=1
    print(f"stock: {stock}, dia {dia}")
    dia +=1
if(sinstock>0):
    print(f"Durante los ciclos hubo {sinstock} dias sin stock")
else:
    print("No hubo dias sin stock.")
if(restock>0):
    print(f"Hubo {restock} restocks en la tienda.")
else:
    print("no hubo restock.")