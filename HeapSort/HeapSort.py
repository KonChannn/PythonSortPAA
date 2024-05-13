import time

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) 
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)

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
        heapSort(arr)
        end_time = time.time()
        execution_time = end_time - start_time

        write_data_to_file(output_file, arr)

        with open("exectime.txt", 'a') as exectime:
            exectime.write(f"Execution Time for {num_data} data: {execution_time:.6f} seconds\n")
