import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def simular():
    try:
        individuos = int(entry_individuos.get())
        muertes = int(entry_muertes.get())
        nacimientos = int(entry_nacimientos.get())
        periodo = int(entry_periodo.get())
    except ValueError:
        messagebox.showerror("Error", "Todos los valores deben ser números")
        return

    is_superior_a_70 = False
    message_superior_a_70 = ""
    xaxis = []
    yaxis = []

    for i in range(1, periodo + 1):
        individuos = individuos - muertes + nacimientos
        xaxis.append(individuos)
        yaxis.append(i)

        if individuos >= 70 and not is_superior_a_70:
            message_superior_a_70 = f"En el período {i}, la población alcanzó 70 individuos."
            is_superior_a_70 = True

    plt.plot(xaxis, yaxis)
    plt.xlabel("Individuos")
    plt.ylabel("Período")
    plt.title("Simulación de Población")
    plt.show()

    resultado = f"Población final: {individuos}"
    if is_superior_a_70:
        resultado += "\n" + message_superior_a_70

    messagebox.showinfo("Resultado", resultado)


# Ventana
root = tk.Tk()
root.title("Simulación de Población")

tk.Label(root, text="Individuos iniciales").pack()
entry_individuos = tk.Entry(root)
entry_individuos.insert(0, "50")
entry_individuos.pack()

tk.Label(root, text="Muertes por período").pack()
entry_muertes = tk.Entry(root)
entry_muertes.insert(0, "2")
entry_muertes.pack()

tk.Label(root, text="Nacimientos por período").pack()
entry_nacimientos = tk.Entry(root)
entry_nacimientos.insert(0, "5")
entry_nacimientos.pack()

tk.Label(root, text="Períodos").pack()
entry_periodo = tk.Entry(root)
entry_periodo.insert(0, "3")
entry_periodo.pack()

tk.Button(root, text="Simular", command=simular).pack(pady=10)

root.mainloop()
