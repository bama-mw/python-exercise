# Membaca nilai x, y, dan z
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))
z = int(input("Masukkan nilai z: "))

# Proses pertukaran nilai
temp = x
x = y
y = z
z = temp

# Menampilkan hasil setelah pertukaran
print(f"Nilai setelah pertukaran: x = {x}, y = {y}, z = {z}")
