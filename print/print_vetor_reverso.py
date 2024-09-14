import sys
import os

# Obtém o caminho absoluto do diretório onde o script está sendo executado
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Adiciona o diretório pai ao sys.path
diretorio_pai = os.path.dirname(diretorio_script)
sys.path.insert(0, diretorio_pai)

import timeit
import random
from funcoes.bubble_sort import BubbleSort
from funcoes.insertion_sort import InsertionSort
from funcoes.quick_sort import QuickSort
from funcoes.counting_sort import CountingSort
from funcoes.heap_sort import HeapSort
from funcoes.merge_sort import MergeSort
from vetores.vetor_reverso import vetor_reverso

# Defina os tamanhos de vetores e o intervalo
inc = 1000
fim = 20000
stp = 1000

# Gere vetores aleatórios
vetores_reversos = vetor_reverso(inc, fim, stp)

print("[[SORTED]]")
print("n    Bubble    Insertion    Merge    Heap   Quick    Counting")

for tamanho, vetores in vetores_reversos.items():
    # Bubble Sort
    inicio = timeit.default_timer()
    for vetor in [vetores]:  # Apenas um vetor por vez
        print(tamanho, end="")
        BubbleSort.bubble_sort(vetor)
    fim = timeit.default_timer()
    print(f" {fim - inicio:7.6f}", end="")

    # Insertion Sort
    inicio = timeit.default_timer()
    for vetor in [vetores]:
        InsertionSort.insertion_sort(vetor)
    fim = timeit.default_timer()
    print(f" {fim - inicio:10.6f}", end="")

    # Merge Sort
    inicio = timeit.default_timer()
    for vetor in [vetores]:
        MergeSort.mergeSort(vetor, 0, len(vetor) - 1)
    fim = timeit.default_timer()
    print(f" {fim - inicio:7.6f}", end="")

    # Heap Sort
    inicio = timeit.default_timer()
    for vetor in [vetores]:
        HeapSort.heap_sort(vetor)
    fim = timeit.default_timer()
    print(f" {fim - inicio:7.6f}", end="")

    # Quick Sort
    inicio = timeit.default_timer()
    for vetor in [vetores]:
        QuickSort.quick_sort(vetor, 0, len(vetor) - 1)
    fim = timeit.default_timer()
    print(f" {fim - inicio:7.6f}", end="")

    # Counting Sort
    inicio = timeit.default_timer()
    for vetor in [vetores]:
        CountingSort.counting_sort(vetor)
    fim = timeit.default_timer()
    print(f" {fim - inicio:7.6f}", end="")

    print("\n")
