def vetor_reverso(inc, fim, stp):
    vetores = {}
    
    for n in range(inc, fim + 1, stp):
        vetor = [i for i in range(n, 0, -stp)]
        vetores[n] = vetor
        
    return vetores

