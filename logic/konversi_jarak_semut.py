def konversi_jarak(x):
    # Menghitung kilometer
    kilometer = x // 100000
    
    # Sisa dalam sentimeter setelah dikonversi ke kilometer
    sisa_cm = x % 100000
    
    # Menghitung meter
    meter = sisa_cm // 100
    
    # Sisa sentimeter setelah dikonversi ke meter
    sisa_cm = sisa_cm % 100
    
    # Menampilkan hasil konversi
    print(f"{kilometer} km + {meter} m + {sisa_cm} cm")

# Contoh penggunaan
x = 261341  # jarak dalam sentimeter
konversi_jarak(x)
