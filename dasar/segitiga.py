print("===========================")
print("PROGRAM SEGITIGA")
print("===========================")

tinggi = float(input("Masukkan tinggi: "))
alas = float(input("Masukkan alas: "))

luas = 0.5 * alas * tinggi
keliling = alas + 2 * (tinggi**2 + (alas/2)**2)**0.5

print(f"Luas: {luas} cm2")
print(f"Keliling: {keliling} cm")