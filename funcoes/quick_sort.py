
import sys
sys.setrecursionlimit(10000)

class QuickSort:

    @staticmethod
    def partition(A, p, r):
        x = A[r]  # Escolhe o pivô como o último elemento
        i = p - 1  # Define o índice para os elementos menores que o pivô

        for j in range(p, r):  # Itera do início ao penúltimo elemento
            if A[j] <= x:  # Se o elemento atual for menor ou igual ao pivô
                i += 1
                A[i], A[j] = A[j], A[i]  # Troca A[i] com A[j]

        A[i + 1], A[r] = A[r], A[i + 1]  # Coloca o pivô na posição correta
        return i + 1  # Retorna a posição do pivô

    @staticmethod
    def quick_sort(A, p, r):
        if p < r:  # Condição de parada: quando o subarray tem mais de um elemento
            q = QuickSort.partition(A, p, r)  # Particiona o array e obtém a posição do pivô
            QuickSort.quick_sort(A, p, q - 1)  # Ordena a primeira metade
            QuickSort.quick_sort(A, q + 1, r)  # Ordena a segunda metade
