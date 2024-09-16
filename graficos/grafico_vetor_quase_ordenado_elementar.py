import matplotlib.pyplot as plt

def grafico_vetores_quase_ordenados(tamanhos_vetores, tempo_bubble, tempo_insertion):
    plt.plot(tamanhos_vetores, tempo_bubble, label='Bubble', marker='+', color='purple')
    plt.plot(tamanhos_vetores, tempo_insertion, label='Insertion', marker='x', color='green')

    plt.title('Algoritmos Elementares - Vetor Quase Ordenado')
    plt.xlabel('n')
    plt.ylabel('Tempo (s)')

    plt.legend()
    plt.show()

tamanho_vetor = [2000, 4000, 6000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
tempo_bubble = [0.061524, 0.257124, 0.587552, 1.054163, 1.335731, 1.652692, 2.001550, 2.374910, 2.807311, 3.265598]
tempo_insertion = [0.000102, 0.000213, 0.000318, 0.000426, 0.000475, 0.000525, 0.000586, 0.000645, 0.000692, 0.000771]

grafico_vetores_quase_ordenados(tamanho_vetor, tempo_bubble, tempo_insertion)