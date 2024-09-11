import random

def vetor_aleatorio(inc, fim, stp):
    vetores = {}
    
    for n in range(inc, fim + 1, stp):
        vetor = [random.randint(0, n**2) for _ in range(n)]
        vetores[n] = vetor
        
    return vetores

