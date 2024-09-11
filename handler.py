import random
import time 
import timeit
from funcoes.bubble_sort import bubble_sort 
from funcoes.insertion_sort import insertion_sort

def vetor_aleatorio(inc, fim, stp):
    vetores = {}
    
    for n in range(inc, fim + 1, stp):
        vetor = [random.randint(0, n**2) for _ in range(n)]
        vetores[n] = vetor
        
    return vetores

def vetor_reverso(inc, fim, stp):
    vetores = {}
    
    for n in range(inc, fim + 1, stp):
        vetor = [i for i in range(n, 0, -stp)]
        vetores[n] = vetor
        
    return vetores

#EXAMPLE
inc = 1000
fim = 20000
stp = 1000

vetores_aleatorios = vetor_aleatorio(inc, fim, stp)
vetores_reversos = vetor_reverso(inc, fim, stp)

# Exibindo vetores reversos
print("[[REVERSO]]")
for n, vetor in vetores_reversos.items():
    print(f"Vetor reverso com {n} elementos: {vetor[:5]}...")

''' 
# Exibindo um exemplo de vetor gerado

for n, vetor in vetores_gerados.items(0):
    print(f"Vetor com {n} elementos: {vetor[:5]}...")  
'''

print("[[RANDOM]]")
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    bubble_sort(vetor)
    break
fim = timeit.default_timer()
print ('duracao bubble sort: %f' % (fim - inicio))
#print(vetor)

#---------------------------------Insertion--------------------
inicio = timeit.default_timer()
for n, vetor in vetores_aleatorios.items():
    insertion_sort(vetor)
    break
fim = timeit.default_timer()
print ('duracao insertion sort: %f' % (fim - inicio))
#print(vetor)



