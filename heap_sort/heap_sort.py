def heapify(vector, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and vector[i] < vector[l]:
        largest = l
    if r < n and vector[largest] < vector[r]:
        largest = r
    if largest != i:
        vector[i],vector[largest] = vector[largest],vector[i] # swap    
        heapify(vector, n, largest)

def heap_sort(vector):
    n = len(vector)
    for i in range(n, -1, -1):
        heapify(vector, n, i)
    for i in range(n-1, 0, -1):
        vector[i], vector[0] = vector[0], vector[i] # swap
        heapify(vector, i, 0)
    return vector
