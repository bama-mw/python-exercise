# Fungsi untuk menghitung berat badan ideal
def hitung_berat_ideal(tinggi_badan):
    # Menghitung hasil pertama (tinggi badan - 100)
    hasil_pertama = tinggi_badan - 100
    
    # Menghitung 10% dari hasil pertama
    sepuluh_persen = hasil_pertama * 0.10
    
    # Menghitung berat badan ideal
    berat_ideal = hasil_pertama - sepuluh_persen
    
    # Mengembalikan hasil berat badan ideal
    return berat_ideal

# Input tinggi badan dari pengguna
tinggi_badan = float(input("Masukkan tinggi badan (dalam cm): "))

# Menentukan berat badan ideal
berat_ideal = hitung_berat_ideal(tinggi_badan)

# Menampilkan hasil
print(f"Berat badan ideal untuk tinggi {tinggi_badan} cm adalah {berat_ideal:.2f} kg.")
