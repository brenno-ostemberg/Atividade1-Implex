#Brenno Ostemberg - Júlia Campos
def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j] 
    return vetor

def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        key = vetor[i]
        j = i - 1
        while j >= 0 and key < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = key
    return vetor
