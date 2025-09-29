def tukar_uang(uang):
    pecahan = [1000, 500, 100, 50, 25]
    for p in pecahan:
        jumlah_pecahan = uang // p  # Menghitung jumlah pecahan yang digunakan
        uang = uang % p  # Menghitung sisa uang setelah pecahan dipakai
        if jumlah_pecahan > 0:
            print(f"Jumlah pecahan Rp{p}: {jumlah_pecahan}")

# Contoh penggunaan
uang = 2775
tukar_uang(uang)
