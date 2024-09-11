import random
import time 
import timeit
from funcoes.bubble_sort import bubble_sort 

def gerar_vetores(inc, fim, stp):
    vetores = {}
    
    for n in range(inc, fim + 1, stp):
        vetor = [random.randint(0, n**2) for _ in range(n)]
        vetores[n] = vetor
        
    return vetores

#EXAMPLE
inc = 1000
fim = 20000
stp = 1000
vetores_gerados = gerar_vetores(inc, fim, stp)

''' Exibindo um exemplo de vetor gerado
for n, vetor in vetores_gerados.items(0):
    print(f"Vetor com {n} elementos: {vetor[:5]}...")  
'''

print("[[RANDOM]]")
inicio = timeit.default_timer()

for n, vetor in vetores_gerados.items():
    bubble_sort(vetor)
    break

fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))

