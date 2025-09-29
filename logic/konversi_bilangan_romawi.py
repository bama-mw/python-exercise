def konversi_romawi(n):
    # Daftar pasangan nilai romawi
    romawi_nilai = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    
    hasil = ""
    
    # Mengonversi bilangan ke dalam angka romawi
    for nilai, simbol in romawi_nilai:
        while n >= nilai:
            hasil += simbol
            n -= nilai
    
    return hasil

# Input dari pengguna
n = int(input("Masukkan bilangan bulat positif: "))

# Mengonversi bilangan dan menampilkan hasil
print(f"Angka Romawi dari {n} adalah {konversi_romawi(n)}")
