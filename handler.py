import random

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
for n, vetor in vetores_gerados.items():
    print(f"Vetor com {n} elementos: {vetor[:5]}...")  

'''
print("[[RANDOM]]")

