import random
from vetores.vetor_ordenado import vetor_ordenado

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