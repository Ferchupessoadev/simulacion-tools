import matplotlib.pyplot as plt
import numpy as np

def main():
    individuos = 50
    muertes_por_periodo = 2
    nacimientos_por_periodo = 5
    periodo = int(input("Digite o período (1, 2 ou 3): "))
    is_superior_a_70 = False
    message_superior_a_70 = ""
    xaxis = np.array([])
    yaxis = np.array([])
    for i in range(1, periodo + 1):
        individuos = individuos - muertes_por_periodo + nacimientos_por_periodo
        xaxis = np.append(xaxis, individuos)
        yaxis = np.append(yaxis, i)
        print(f"Período {i}: {individuos} indivíduos")
        if individuos >= 70 and not is_superior_a_70:
            message_superior_a_70 = f"\nEn el período {i}, la población ha alcanzado o superado los 70 individuos.\n"
            is_superior_a_70 = True
    
    plt.plot(xaxis, yaxis)
    fig = plt.gcf()
    fig.canvas.manager.set_window_title('Simulación de Población')
    plt.xlabel("Individuos")
    plt.ylabel("Período")
    plt.title("Simulación de Población")
    plt.show()
    print(f"Población final después de {periodo} períodos: {individuos} indivíduos")
    if is_superior_a_70:
        print(message_superior_a_70)

if __name__ == "__main__":
    main()
