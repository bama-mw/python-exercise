def hitung_selisih_tanggal(tanggal1, tanggal2):
    # Fungsi untuk menghitung total hari dari sebuah tanggal
    def konversi_ke_hari(dd, mm, yy):
        return (yy * 365) + (mm * 30) + dd

    # Ekstrak tanggal, bulan, tahun dari tanggal1 dan tanggal2
    dd1, mm1, yy1 = tanggal1
    dd2, mm2, yy2 = tanggal2

    # Hitung total hari untuk masing-masing tanggal
    total_hari1 = konversi_ke_hari(dd1, mm1, yy1)
    total_hari2 = konversi_ke_hari(dd2, mm2, yy2)

    # Hitung selisih hari
    selisih_hari = abs(total_hari2 - total_hari1)

    # Konversi selisih hari ke tahun, bulan, dan hari
    tahun = selisih_hari // 365
    sisa_hari = selisih_hari % 365
    bulan = sisa_hari // 30
    hari = sisa_hari % 30

    return tahun, bulan, hari

# Input tanggal dalam format (dd, mm, yy)
tanggal1 = (1, 1, 2000)  # Contoh input
tanggal2 = (15, 3, 2002) # Contoh input

# Hitung selisih
tahun, bulan, hari = hitung_selisih_tanggal(tanggal1, tanggal2)

# Tampilkan hasil
print(f"Selisih: {tahun} tahun, {bulan} bulan, {hari} hari")
