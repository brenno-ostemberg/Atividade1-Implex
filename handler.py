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
from vetores.vetor_quase_ordenado import vetor_quase_ordenado

#EXAMPLE
inc = 1000
fim = 20000
stp = 1000

vetores_aleatorios = vetor_aleatorio(inc, fim, stp)
vetores_reversos = vetor_reverso(inc, fim, stp)
vetores_ordenados = vetor_ordenado(inc, fim, stp)
vetores_quase_ordenados = vetor_quase_ordenado(inc, fim, stp)
'''
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

print("[[NEARLY SORTED]]")
for n, vetor in vetores_quase_ordenados.items():
    print(f"Vetor quase ordenado com {n} elementos: {vetor[:5]}...")

''' 
# Exibindo um exemplo de vetor gerado

print("[[REVERSE]]")
for n, vetor in vetores_reversos.items():
    print(f"Vetor reverso com {n} elementos: {vetor[:50]}")


print("[[RANDOM]]")
print("n    Bubble    Insertion    Merge     Heap       Quick      Counting")

inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    print(n, end="")
    BubbleSort.bubble_sort(vetor)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end=" ")

#---------------------------------Insertion--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    InsertionSort.insertion_sort(vetor)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end="   ")


#---------------------------------merge--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    MergeSort.mergeSort(vetor, 0, len(vetor)-1)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end="  ")

#---------------------------------heap--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    HeapSort.heap_sort(vetor)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end="  ")


#---------------------------------quick--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    QuickSort.quick_sort(vetor, 0, len(vetor) - 1)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end="  ")

#---------------------------------counting--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    CountingSort.counting_sort(vetor)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end="  ")

print("\n")
#---------------------------------------fim vetor 1000---------------

inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    print(n, end="")
    BubbleSort.bubble_sort(vetor)
  
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end=" ")
'''
#---------------------------------Insertion--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    InsertionSort.insertion_sort(vetor)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end="   ")


#---------------------------------merge--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    MergeSort.mergeSort(vetor, 0, len(vetor)-1)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end="  ")

#---------------------------------heap--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    HeapSort.heap_sort(vetor)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end="  ")


#---------------------------------quick--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    QuickSort.quick_sort(vetor, 0, len(vetor) - 1)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end="  ")

#---------------------------------counting--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    CountingSort.counting_sort(vetor)
    break
fim = timeit.default_timer()
print (' %f' % (fim - inicio), end="  ")

print("\n")

'''