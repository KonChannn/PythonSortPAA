import time

def count_sort(input_array):
	# Finding the maximum element of input_array.
	M = max(input_array)

	# Initializing count_array with 0
	count_array = [0] * (M + 1)

	# Mapping each element of input_array as an index of count_array
	for num in input_array:
		count_array[num] += 1

	# Calculating prefix sum at every index of count_array
	for i in range(1, M + 1):
		count_array[i] += count_array[i - 1]

	# Creating output_array from count_array
	output_array = [0] * len(input_array)

	for i in range(len(input_array) - 1, -1, -1):
		output_array[count_array[input_array[i]] - 1] = input_array[i]
		count_array[input_array[i]] -= 1

	return output_array


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
        output_array = count_sort(arr)
        end_time = time.time()
        execution_time = end_time - start_time

        write_data_to_file(output_file, output_array)

        with open("exectime.txt", 'a') as exectime:
            exectime.write(f"Execution Time for {num_data} data: {execution_time:.6f} seconds\n")
