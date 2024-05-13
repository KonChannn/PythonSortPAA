import time

def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position

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
        insertionSort(arr)
        end_time = time.time()
        execution_time = end_time - start_time

        write_data_to_file(output_file, arr)

        with open("exectime.txt", 'a') as exectime:
            exectime.write(f"Execution Time for {num_data} data: {execution_time:.6f} seconds\n")
