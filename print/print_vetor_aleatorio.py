import sys
import os

# Adicionando o diretório pai ao path
diretorio_script = os.path.dirname(os.path.abspath(__file__))

diretorio_pai = os.path.dirname(diretorio_script)
sys.path.insert(0, diretorio_pai)

# Importando as funções
import timeit
from funcoes.bubble_sort import BubbleSort
from funcoes.insertion_sort import InsertionSort
from funcoes.quick_sort import QuickSort
from funcoes.counting_sort import CountingSort
from funcoes.heap_sort import HeapSort
from funcoes.merge_sort import MergeSort
from vetores.vetor_aleatorio import vetor_aleatorio

'''
# Valores do Teste
inc = 1000
fim = 13000
stp = 1000
'''

# Função que printa a execução dos algoritmos de ordenação com vetores aleatórios
def printar_execucao_vetor_aleatorio(inc, fim, stp):

    # Criando o vetor aleatório
    vetores_aleatorios = vetor_aleatorio(inc, fim, stp)

    # Exibindo na tela os algoritmos de ordenação com seus respectivos tempos
    print("[[RANDOM]]")
    print("n    Bubble    Insertion    Merge    Heap   Quick    Counting")

    for tamanho, vetores in vetores_aleatorios.items():
        inicio = timeit.default_timer()
        for vetor in [vetores]: 
            print(tamanho, end="")
            BubbleSort.bubble_sort(vetor)
        fim = timeit.default_timer()
        print(f" {fim - inicio:7.6f}", end="")

        inicio = timeit.default_timer()
        for vetor in [vetores]:
            InsertionSort.insertion_sort(vetor)
        fim = timeit.default_timer()
        print(f" {fim - inicio:10.6f}", end="")

        inicio = timeit.default_timer()
        for vetor in [vetores]:
            MergeSort.mergeSort(vetor, 0, len(vetor) - 1)
        fim = timeit.default_timer()
        print(f" {fim - inicio:7.6f}", end="")

        inicio = timeit.default_timer()
        for vetor in [vetores]:
            HeapSort.heap_sort(vetor)
        fim = timeit.default_timer()
        print(f" {fim - inicio:7.6f}", end="")

        inicio = timeit.default_timer()
        for vetor in [vetores]:
            QuickSort.quick_sort(vetor, 0, len(vetor) - 1)
        fim = timeit.default_timer()
        print(f" {fim - inicio:7.6f}", end="")

        inicio = timeit.default_timer()
        for vetor in [vetores]:
            CountingSort.counting_sort(vetor, max(vetor))
        fim = timeit.default_timer()
        print(f" {fim - inicio:7.6f}", end="")

        print("\n")

'''
# Chamando a função
printar_execucao_vetor_aleatorio(inc, fim, stp)
'''