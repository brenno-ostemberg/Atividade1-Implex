def vetor_ordenado(inc, fim, stp):
    vetores = {}
    
    for n in range(inc, fim + 1, stp):
        vetor = [i for i in range(1, n + 1)]
        vetores[n] = vetor
        
    return vetores