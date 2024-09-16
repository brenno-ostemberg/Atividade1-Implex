import matplotlib.pyplot as plt

def grafico_vetores_reversos(tamanhos_vetores, tempo_bubble, tempo_insertion):
    plt.plot(tamanhos_vetores, tempo_bubble, label='Bubble', marker='+', color='purple')
    plt.plot(tamanhos_vetores, tempo_insertion, label='Insertion', marker='x', color='green')

    plt.title('Algoritmos de Ordenação - Vetor Reverso')
    plt.xlabel('n')
    plt.ylabel('Tempo (s)')

    plt.legend()
    plt.show()

tamanho_vetor = [2000, 4000, 6000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
tempo_bubble = [0.125140, 0.521831, 1.190485, 2.137446, 2.694885, 3.351709, 4.027694, 4.792865, 5.675612, 6.542949]
tempo_insertion = [0.000101, 0.000211, 0.000325, 0.000428, 0.000480, 0.000530, 0.000582, 0.000621, 0.000715, 0.000751]

grafico_vetores_reversos(tamanho_vetor, tempo_bubble, tempo_insertion)