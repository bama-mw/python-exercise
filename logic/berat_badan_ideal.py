def cek_berat_badan_ideal(BB, TB):
    # Menghitung berat badan ideal berdasarkan tinggi badan
    BB_ideal = TB - 100
    
    # Menghitung selisih antara berat badan yang diberikan dan berat badan ideal
    selisih = abs(BB - BB_ideal)
    
    # Menentukan apakah berat badan ideal atau tidak
    if selisih <= 2:
        return "ideal"
    else:
        return "tidak ideal"

# Input berat badan dan tinggi badan
BB = float(input("Masukkan berat badan (kg): "))
TB = float(input("Masukkan tinggi badan (cm): "))

# Menampilkan hasil
hasil = cek_berat_badan_ideal(BB, TB)
print("Status berat badan: ", hasil)
