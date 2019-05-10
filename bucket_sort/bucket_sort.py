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

def insertionSort(vector): 
	for i in range(1, len(vector)): 
		up = vector[i] 
		j = i - 1
		while j >=0 and vector[j] > up: 
			vector[j + 1] = vector[j] 
			j -= 1
		vector[j + 1] = up	 
	return vector
			
def iterative_bucket_sort(vector): 
	arr = [] 
	number_buckets = 10
	for i in range(number_buckets): 
		arr.append([]) 
		
	for j in  range(0, len(vector)):
		str_vec = str(vector[j])
		dif = len(str(max(vector))) - len(str(vector[j]))
		str_vec = '0' * dif + str_vec
		sig = int(str_vec[0])
		arr[sig].append(vector[j])
	
	for i in range(number_buckets): 
		arr[i] = insertionSort(arr[i]) 
		
	k = 0
	for i in range(number_buckets): 
		for j in range(len(arr[i])): 
			vector[k] = arr[i][j] 
			k += 1
	return vector

def bucket_radix_sort(vector): 
	arr = [] 
	number_buckets = 10
	for i in range(number_buckets): 
		arr.append([]) 
		
	for j in  range(0, len(vector)):
		str_vec = str(vector[j])
		dif = len(str(max(vector))) - len(str(vector[j]))
		str_vec = '0' * dif + str_vec
		sig = int(str_vec[0])
		arr[sig].append(vector[j])
	
	for i in range(number_buckets): 
		arr[i] = radix_sort(arr[i]) 
		
	k = 0
	for i in range(number_buckets): 
		for j in range(len(arr[i])): 
			vector[k] = arr[i][j] 
			k += 1
	return vector