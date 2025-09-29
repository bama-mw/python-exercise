def cek_jenis_segitiga(a, b, c):
    # Pastikan a <= b <= c
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    
    # Menggunakan hukum Pythagoras untuk menentukan jenis segitiga
    if a**2 + b**2 == c**2:
        return "Segitiga Siku-siku"
    elif a**2 + b**2 > c**2:
        return "Segitiga Lancip"
    else:
        return "Segitiga Tumpul"

# Input tiga sisi segitiga
a = int(input("Masukkan sisi a: "))
b = int(input("Masukkan sisi b: "))
c = int(input("Masukkan sisi c: "))

# Cek dan tampilkan jenis segitiga
print(cek_jenis_segitiga(a, b, c))
