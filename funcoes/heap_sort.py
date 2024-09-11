def swap(arr:list, i:int, j:int) -> None:
    arr[i], arr[j] = arr[j], arr[i]

def heapify(vetor, n, i):
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # left = 2*i + 1
    right = 2 * i + 2    # right = 2*i + 2

    # If left child is larger than root
    if left < n and vetor[left] > vetor[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and vetor[right] > vetor[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        swap(vetor[i], vetor[largest])

        # Recursively heapify the affected sub-tree
        heapify(vetor, n, largest)

def heap_sort(vetor):

    n = len(vetor)
    
    #array of length 1 is by default sorted
    if n <= 1:
        return vetor

    # Build a maxheap.
    for i in range((n - 1)//2, -1, -1):
        heapify(vetor, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        swap(vetor,i,0)  # swap
        heapify(vetor, i, 0)

    return vetor