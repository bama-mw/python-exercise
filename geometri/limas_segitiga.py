# Dibuat Oleh : Bama Maulana Wibisana
# Tanggal Pengerjaan : 08 Oktober 2024
# Program Menghitung Rumus Limas Segitiga

print("="*20)
print("Rumus Limas Segitiga")
print("="*20)

a = int(input("Alas\t: "))
ts = int(input("Tinggi Segitiga\t: "))
tl = int(input("Tinggi Limas\t: "))
s1 = int(input("Sisi 1\t: "))
s2 = int(input("Sisi 2\t: "))
s3 = int(input("Sisi 3\t: "))

la = 1/2 * a * ts
ls1 = 1/2 * a * s1
ls2 = 1/2 * a * s2
ls3 = 1/2 * a * s3

lp = la + ls1 + ls2 + ls3
v = 1/3 * la * tl

print(f"Luas Permukaan\t: {lp}")
print(f"Volume\t\t: {round(v, 2)}")