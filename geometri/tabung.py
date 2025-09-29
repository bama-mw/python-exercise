# Dibuat Oleh : Bama Maulana Wibisana
# Tanggal Pengerjaan : 08 Oktober 2024
# Program Menghitung Rumus Tabung

print("="*20)
print("Rumus Tabung")
print("="*20)

r = int(input("Jari-jari\t: "))
t = int(input("Tinggi\t\t: "))

lp = 2 * 3.14 * r * (r + t)
ls = 2 * 3.14 * r * t
v = 3.14 * r * r * t

print(f"Luas Permukaan\t: {lp}")
print(f"Luas Selimut\t: {ls}")
print(f"Volume\t\t: {v}")