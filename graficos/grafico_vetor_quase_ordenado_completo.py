import matplotlib.pyplot as plt

def grafico_vetores_quase_ordenados(tamanhos_vetores, tempo_bubble, tempo_insertion, tempo_merge, tempo_heap, tempo_quick, tempo_counting):
    plt.plot(tamanhos_vetores, tempo_bubble, label='Bubble', marker='+', color='purple')
    plt.plot(tamanhos_vetores, tempo_insertion, label='Insertion', marker='x', color='green')
    plt.plot(tamanhos_vetores, tempo_merge, label='Merge', marker='*', color='blue')
    plt.plot(tamanhos_vetores, tempo_heap, label='Heap', marker='s', fillstyle='none', color='orange')
    plt.plot(tamanhos_vetores, tempo_quick, label='Quick', marker='s', color='yellow')
    plt.plot(tamanhos_vetores, tempo_counting, label='Counting', marker='o', fillstyle='none', color='red')

    plt.title('Algoritmos de Ordenação - Vetor Quase Ordenado')
    plt.xlabel('n')
    plt.ylabel('Tempo (s)')

    plt.legend()
    plt.show()

tamanho_vetor = [2000, 4000, 6000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
tempo_bubble = [0.061524, 0.257124, 0.587552, 1.054163, 1.335731, 1.652692, 2.001550, 2.374910, 2.807311, 3.265598]
tempo_insertion = [0.000102, 0.000213, 0.000318, 0.000426, 0.000475, 0.000525, 0.000586, 0.000645, 0.000692, 0.000771]
tempo_merge = [0.002424, 0.005148, 0.008003, 0.010887, 0.012427, 0.013989, 0.015494, 0.016988, 0.018654, 0.020084]
tempo_heap = [0.003610, 0.008755, 0.012753, 0.017794, 0.020018, 0.022317, 0.025246, 0.027316, 0.030150, 0.032778]
tempo_quick = [0.092706, 0.384402, 0.876042, 1.567770, 1.983582, 2.453853, 2.967144, 3.532206, 4.150893, 4.802483]
tempo_counting = [0.000289, 0.000566, 0.000897, 0.001210, 0.001421, 0.001507, 0.001713, 0.001900, 0.002003, 0.002098]

grafico_vetores_quase_ordenados(tamanho_vetor, tempo_bubble, tempo_insertion, tempo_merge, tempo_heap, tempo_quick, tempo_counting)