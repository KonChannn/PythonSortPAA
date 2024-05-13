import matplotlib.pyplot as plt

# Data running time dan jumlah data
data = [
    (1000, 0.001234),  # Contoh data, ganti dengan hasil eksekusi Anda
    (2000, 0.002345),
    (3000, 0.003456),
    (4000, 0.004567),
    (5000, 0.005678)
]

# Pisahkan jumlah data dan running time
num_data, execution_time = zip(*data)

# Buat grafik
plt.plot(num_data, execution_time, marker='o', linestyle='-')
plt.title('Running Time vs Number of Data')
plt.xlabel('Number of Data')
plt.ylabel('Running Time (seconds)')
plt.grid(True)
plt.show()
