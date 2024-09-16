import matplotlib.pyplot as plt

def grafico_vetores_ordenados(tamanhos_vetores, tempo_bubble, tempo_insertion):
    plt.plot(tamanhos_vetores, tempo_bubble, label='Bubble', marker='+', color='purple')
    plt.plot(tamanhos_vetores, tempo_insertion, label='Insertion', marker='x', color='green')

    plt.title('Algoritmos de Ordenação - Vetor Ordenado')
    plt.xlabel('n')
    plt.ylabel('Tempo (s)')

    plt.legend()
    plt.show()

tamanho_vetor = [2000, 4000, 6000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
tempo_bubble = [0.052687, 0.233660, 0.534109, 0.955632, 1.206926, 1.496958, 1.805852, 2.149473, 2.518621, 2.926628]
tempo_insertion = [0.000108, 0.000213, 0.000322, 0.000433, 0.000476, 0.000547, 0.000596, 0.000638, 0.000714, 0.000746]

grafico_vetores_ordenados(tamanho_vetor, tempo_bubble, tempo_insertion)