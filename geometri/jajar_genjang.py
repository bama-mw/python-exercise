# Dibuat Oleh : Bama Maulana Wibisana
# Tanggal Pengerjaan : 08 Oktober 2024
# Program Menghitung Rumus Jajar Genjang

print("="*20)
print("Rumus Jajar Genjang")
print("="*20)

a = int(input("Alas\t\t: "))
t = int(input("Tinggi\t\t: "))
sm = int(input("Sisi Miring\t: "))

l = a * t
k = 2 * (a + sm)

print(f"Luas\t\t: {l}")
print(f"Keliling\t: {k}")   