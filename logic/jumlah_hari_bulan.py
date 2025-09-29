def jumlah_hari(bulan, tahun):
    # Daftar jumlah hari dalam bulan biasa (non-kabisat)
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Memeriksa tahun kabisat
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        hari_per_bulan[1] = 29  # Februari menjadi 29 hari jika tahun kabisat
    
    # Mengembalikan jumlah hari di bulan yang diberikan (bulan-1 karena index mulai dari 0)
    return hari_per_bulan[bulan - 1]

# Input bulan dan tahun
bulan = int(input("Masukkan nomor bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

# Menampilkan jumlah hari dalam bulan tersebut
jumlah = jumlah_hari(bulan, tahun)
print(f"Jumlah hari di bulan {bulan} tahun {tahun} adalah {jumlah} hari.")
