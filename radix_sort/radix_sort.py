def radix_sort(vector, base=10):
    if vector == []:
        return
 
    def key_factory(digit, base):
        def key(vector, index):
            return ((vector[index]//(base**digit)) % base)
        return key
    largest = max(vector)
    exp = 0
    while base**exp <= largest:
        vector = counting_sort(vector, base - 1, key_factory(exp, base))
        exp = exp + 1
    return vector
 
def counting_sort(vector, largest, key):
    c = [0]*(largest + 1)
    for i in range(len(vector)):
        c[key(vector, i)] = c[key(vector, i)] + 1
 
    # Find the last index for each element
    c[0] = c[0] - 1 # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
 
    result = [None]*len(vector)
    for i in range(len(vector) - 1, -1, -1):
        result[c[key(vector, i)]] = vector[i]
        c[key(vector, i)] = c[key(vector, i)] - 1
 
    return result


vector = [12,23,4,5,5123,34,34543,543,53,434313,4,1,0]
sorted_list = radix_sort(vector)
print(sorted_list)