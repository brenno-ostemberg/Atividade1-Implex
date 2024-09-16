import matplotlib.pyplot as plt

def grafico_vetores_aleatorios(tamanhos_vetores, tempo_bubble, tempo_insertion):
    plt.plot(tamanhos_vetores, tempo_bubble, label='Bubble', marker='+', color='purple')
    plt.plot(tamanhos_vetores, tempo_insertion, label='Insertion', marker='x', color='green')

    plt.title('Algoritmos de ordenação')
    plt.xlabel('n')
    plt.ylabel('Tempo (s)')

    plt.legend()
    plt.show()

tamanho_vetor = [2000, 4000, 6000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
tempo_bubble = [0.095585, 0.406070, 0.957655, 1.778917, 2.494518, 2.961461, 3.623052, 3.982920, 4.937081, 5.372960]
tempo_insertion = [0.000102, 0.000204, 0.000323, 0.000450, 0.000530, 0.000584, 0.000616, 0.000683, 0.000730, 0.000767]

grafico_vetores_aleatorios(tamanho_vetor, tempo_bubble, tempo_insertion)