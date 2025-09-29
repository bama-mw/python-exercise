def konversi_panjang(panjang_dalam_meter):
    # Konversi ke inci
    konversi_inci = panjang_dalam_meter * (1000 / 25.4)
    
    # Konversi ke kaki
    konversi_kaki = panjang_dalam_meter * (100 / 30.48)
    
    # Konversi ke yard
    konversi_yard = panjang_dalam_meter / 0.9144
    
    # Output hasil konversi
    print(f"Panjang dalam inci: {konversi_inci} inci")
    print(f"Panjang dalam kaki: {konversi_kaki} kaki")
    print(f"Panjang dalam yard: {konversi_yard} yard")

# Contoh penggunaan
panjang_meter = float(input("Masukkan panjang benda dalam meter: "))
konversi_panjang(panjang_meter)
