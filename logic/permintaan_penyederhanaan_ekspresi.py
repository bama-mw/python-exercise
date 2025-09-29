def hitung_m(a, b, c, d):
    # Menghitung nilai m berdasarkan rumus yang diberikan
    m = (a - b) / (3 * a * c) * (1 - b / (c * d))
    return m

# Contoh penggunaan fungsi
a = 10
b = 5
c = 2
d = 4

m = hitung_m(a, b, c, d)
print(f"Nilai m adalah: {m}")
