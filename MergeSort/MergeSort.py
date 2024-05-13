import time

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = [int(line.strip()) for line in file]
    return data

def write_data_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

if __name__ == "__main__":
    input_file = "../case5.txt"
    data_5000 = read_data_from_file(input_file)

    file_prefix = "case"
    file_extension = ".txt"

    for num_data in [1000, 2000, 3000, 4000, 5000]:
        output_file = file_prefix + str(num_data) + file_extension
        arr = data_5000[:num_data]  

        start_time = time.time()
        mergeSort(arr, 0, num_data - 1)
        end_time = time.time()
        execution_time = end_time - start_time

        write_data_to_file(output_file, arr)

        with open("exectime.txt", 'a') as exectime:
            exectime.write(f"Execution Time for {num_data} data: {execution_time:.6f} seconds\n")