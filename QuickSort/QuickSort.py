# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
import time

# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# function to perform quicksort


def quickSort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)


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
        quickSort(arr, 0, num_data - 1)
        end_time = time.time()
        execution_time = end_time - start_time

        write_data_to_file(output_file, arr)

        with open("exectime.txt", 'a') as exectime:
            exectime.write(f"Execution Time for {num_data} data: {execution_time:.6f} seconds\n")

