import radix_sort.radix_sort as radix_sort

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

def bucket_iterative_radix_sort(vector): 
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
		arr[i] = radix_sort.iterative_radix_sort(arr[i]) 
		
	k = 0
	for i in range(number_buckets): 
		for j in range(len(arr[i])): 
			vector[k] = arr[i][j] 
			k += 1
	return vector