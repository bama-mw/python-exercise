def hitung_volume(m):
    # Menghitung volume menggunakan rumus V = (4/3) * m^3
    V = (4/3) * (m ** 3)
    return V

# Contoh penggunaan
massa = float(input("Masukkan nilai massa (m): "))
volume = hitung_volume(massa)
print(f"Volume V untuk massa {massa} adalah {volume}")
