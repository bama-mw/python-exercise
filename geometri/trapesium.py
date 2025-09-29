# Dibuat Oleh : Bama Maulana Wibisana
# Tanggal Pengerjaan : 08 Oktober 2024
# Program Menghitung Rumus Trapesium

print("="*20)
print("Rumus Trapesium")
print("="*20)

s1 = int(input("Sisi Sejajar 1\t\t: "))
s2 = int(input("Sisi Sejajar 2\t\t: "))
s3 = int(input("Sisi Tidak Sejajar 1\t: "))
s4 = int(input("Sisi Tidak Sejajar 2\t: "))
t = int(input("Tinggi\t\t\t: "))

l = 1/2 * (s1 + s2) * t
k = s1 + s2 + s3 + s4

print(f"Luas\t\t\t: {l}")
print(f"Keliling\t\t: {k}")