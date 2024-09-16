import matplotlib.pyplot as plt

def grafico_vetores_reversos(tamanhos_vetores, tempo_merge, tempo_heap, tempo_quick, tempo_counting):
    plt.plot(tamanhos_vetores, tempo_merge, label='Merge', marker='*', color='blue')
    plt.plot(tamanhos_vetores, tempo_heap, label='Heap', marker='s', fillstyle='none', color='orange')
    plt.plot(tamanhos_vetores, tempo_quick, label='Quick', marker='s', color='yellow')
    plt.plot(tamanhos_vetores, tempo_counting, label='Counting', marker='o', fillstyle='none', color='red')

    plt.title('Algoritmos Eficientes - Vetor Reverso')
    plt.xlabel('n')
    plt.ylabel('Tempo (s)')

    plt.legend()
    plt.show()

tamanho_vetor = [2000, 4000, 6000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
tempo_merge = [0.002295, 0.005083, 0.007987, 0.010788, 0.012381, 0.013907, 0.015206, 0.016733, 0.018353, 0.020195]
tempo_heap = [0.003564, 0.007997, 0.012782, 0.017474, 0.019915, 0.022506, 0.027807, 0.027368, 0.030131, 0.033195]
tempo_quick = [0.093155, 0.386239, 0.878284, 1.568707, 1.985186, 2.451767, 2.955118, 3.531088, 4.147042, 4.809883]
tempo_counting = [0.000296, 0.000593, 0.000919, 0.001152, 0.001450, 0.001557, 0.001616, 0.001896, 0.001941, 0.002238]

grafico_vetores_reversos(tamanho_vetor, tempo_merge, tempo_heap, tempo_quick, tempo_counting)