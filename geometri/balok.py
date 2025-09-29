# Dibuat Oleh : Bama Maulana Wibisana
# Tanggal Pengerjaan : 08 Oktober 2024
# Program Menghitung Rumus Balok

print("="*20)
print("Rumus Balok")
print("="*20)

p = int(input("Panjang\t\t: "))
l = int(input("Lebar\t\t: "))
t = int(input("Tinggi\t\t: "))

lp = 2 * (p * l + p * t + l * t)
v = p * l * t
k = 4 * (p + l + t)

print(f"Luas Permukaan\t: {lp}")
print(f"Volume\t\t: {v}")
print(f"Keliling\t: {k}")