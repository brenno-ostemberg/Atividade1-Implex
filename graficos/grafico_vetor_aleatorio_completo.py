import matplotlib.pyplot as plt

def grafico_vetores_aleatorios(tamanhos_vetores, tempo_bubble, tempo_insertion, tempo_merge, tempo_heap, tempo_quick, tempo_counting):
    plt.plot(tamanhos_vetores, tempo_bubble, label='Bubble', marker='+', color='purple')
    plt.plot(tamanhos_vetores, tempo_insertion, label='Insertion', marker='x', color='green')
    plt.plot(tamanhos_vetores, tempo_merge, label='Merge', marker='*', color='blue')
    plt.plot(tamanhos_vetores, tempo_heap, label='Heap', marker='s', fillstyle='none', color='orange')
    plt.plot(tamanhos_vetores, tempo_quick, label='Quick', marker='s', color='yellow')
    plt.plot(tamanhos_vetores, tempo_counting, label='Counting', marker='o', fillstyle='none', color='red')

    plt.title('Algoritmos de Ordenação - Vetor Aleatório')
    plt.xlabel('n')
    plt.ylabel('Tempo (s)')

    plt.legend()
    plt.show()

tamanho_vetor = [2000, 4000, 6000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
tempo_bubble = [0.095585, 0.406070, 0.957655, 1.778917, 2.494518, 2.961461, 3.623052, 3.982920, 4.937081, 5.372960]
tempo_insertion = [0.000102, 0.000204, 0.000323, 0.000450, 0.000530, 0.000584, 0.000616, 0.000683, 0.000730, 0.000767]
tempo_merge = [0.002225, 0.004910, 0.008079, 0.011177, 0.013578, 0.015470, 0.016380, 0.017605, 0.018788, 0.020349]
tempo_heap = [0.003348, 0.008636, 0.012540, 0.018490, 0.021892, 0.024656, 0.026055, 0.028109, 0.030757, 0.033198]
tempo_quick = [0.089118, 0.383530, 0.887803, 1.668525, 2.203390, 2.729839, 3.175095, 3.695912, 4.299218, 4.985924]
tempo_counting = [0.213109, 0.886273, 2.040176, 3.800819, 4.939559, 5.975751, 7.001527, 8.433126, 9.666867, 13.579285]

grafico_vetores_aleatorios(tamanho_vetor, tempo_bubble, tempo_insertion, tempo_merge, tempo_heap, tempo_quick, tempo_counting)