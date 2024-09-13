import random

def vetor_ordenado(inc, fim, stp):
    vetores = {}
    
    for n in range(inc, fim + 1, stp):
        vetor = [i for i in range(1, n + 1)]
        vetores[n] = vetor
        
    return vetores

def vetor_quase_ordenado(inc, fim, stp):
    vetores = vetor_ordenado(inc, fim, stp)
    
    for n, vetor in vetores.items():
        tamanho = len(vetor)
        qtd_embaralhar = max(1, tamanho // 10)
        indices = random.sample(range(tamanho), qtd_embaralhar)
        elementos = [vetor[i] for i in indices]
        random.shuffle(elementos) 
        for i, idx in enumerate(indices):
            vetor[idx] = elementos[i]
    
    return vetores 