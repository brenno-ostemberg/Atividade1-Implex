import random
import timeit
from funcoes.bubble_sort import BubbleSort
from funcoes.insertion_sort import InsertionSort
from funcoes.quick_sort import QuickSort
from funcoes.counting_sort import CountingSort
from funcoes.heap_sort import HeapSort
from funcoes.merge_sort import MergeSort
from vetores.vetor_aleatorio import vetor_aleatorio
from vetores.vetor_reverso import vetor_reverso
from vetores.vetor_ordenado import vetor_ordenado

#EXAMPLE
inc = 1000
fim = 20000
stp = 1000

vetores_aleatorios = vetor_aleatorio(inc, fim, stp)
vetores_reversos = vetor_reverso(inc, fim, stp)
vetores_ordenados = vetor_ordenado(inc, fim, stp)

# Exibindo vetores aleatórios
print("[[RANDOM]]")
for n, vetor in vetores_aleatorios.items():
    print(f"Vetor aleatório com {n} elementos: {vetor[:5]}...")

# Exibindo vetores reversos
print("[[REVERSE]]")
for n, vetor in vetores_reversos.items():
    print(f"Vetor reverso com {n} elementos: {vetor[:5]}...")

# Exibindo vetores ordenados
print("[[SORTED]]")
for n, vetor in vetores_ordenados.items():
    print(f"Vetor ordenado com {n} elementos: {vetor[:5]}...")

''' 
# Exibindo um exemplo de vetor gerado

for n, vetor in vetores_gerados.items(0):
    print(f"Vetor com {n} elementos: {vetor[:5]}...")  
'''

print("[[RANDOM]]")
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    BubbleSort.bubble_sort(vetor)
    break
fim = timeit.default_timer()
print ('duracao bubble sort: %f' % (fim - inicio))
#print(vetor)

#---------------------------------Insertion--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    InsertionSort.insertion_sort(vetor)
    break
fim = timeit.default_timer()
print ('duracao insertion sort: %f' % (fim - inicio))
#print(vetor)



