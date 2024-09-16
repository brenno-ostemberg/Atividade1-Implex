import matplotlib.pyplot as plt

def grafico_vetores_ordenados(tamanhos_vetores, tempo_bubble, tempo_insertion, tempo_merge, tempo_heap, tempo_quick, tempo_counting):
    plt.plot(tamanhos_vetores, tempo_bubble, label='Bubble', marker='+', color='purple')
    plt.plot(tamanhos_vetores, tempo_insertion, label='Insertion', marker='x', color='green')
    plt.plot(tamanhos_vetores, tempo_merge, label='Merge', marker='*', color='blue')
    plt.plot(tamanhos_vetores, tempo_heap, label='Heap', marker='s', fillstyle='none', color='orange')
    plt.plot(tamanhos_vetores, tempo_quick, label='Quick', marker='s', color='yellow')
    plt.plot(tamanhos_vetores, tempo_counting, label='Counting', marker='o', fillstyle='none', color='red')

    plt.title('Algoritmos de Ordenação - Vetor Ordenado')
    plt.xlabel('n')
    plt.ylabel('Tempo (s)')

    plt.legend()
    plt.show()

tamanho_vetor = [2000, 4000, 6000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
tempo_bubble = [0.052687, 0.233660, 0.534109, 0.955632, 1.206926, 1.496958, 1.805852, 2.149473, 2.518621, 2.926628]
tempo_insertion = [0.000108, 0.000213, 0.000322, 0.000433, 0.000476, 0.000547, 0.000596, 0.000638, 0.000714, 0.000746]
tempo_merge = [0.002371, 0.005233, 0.008243, 0.011254, 0.012342, 0.013911, 0.015664, 0.016994, 0.018552, 0.019875]
tempo_heap = [0.003547, 0.008019, 0.012736, 0.017683, 0.019939, 0.022592, 0.028144, 0.027494, 0.029599, 0.033041]
tempo_quick = [0.094055, 0.390669, 0.891957, 1.577434, 1.992990, 2.468324, 2.971398, 3.551046, 4.152136, 4.799707]
tempo_counting = [0.000294, 0.000640, 0.000961, 0.001227, 0.001376, 0.001564, 0.001776, 0.001936, 0.002067, 0.002183]

grafico_vetores_ordenados(tamanho_vetor, tempo_bubble, tempo_insertion, tempo_merge, tempo_heap, tempo_quick, tempo_counting)