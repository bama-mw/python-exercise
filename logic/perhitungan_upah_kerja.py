def hitung_upah(golongan, jam_kerja, jam_lembur=0):
    # Menentukan upah per jam berdasarkan golongan
    if golongan in ['a', 'b', 'c', 'd']:
        upah_per_jam = 4000
    else:
        raise ValueError("Golongan tidak valid")

    # Menghitung upah kerja
    upah_kerja = jam_kerja * upah_per_jam

    # Menghitung upah lembur jika ada
    upah_lembur = 0
    if jam_lembur > 0:
        upah_lembur = jam_lembur * upah_per_jam * 1.5  # Upah lembur 1,5 kali upah per jam normal

    # Menghitung upah total
    upah_total = upah_kerja + upah_lembur
    return upah_total

# Contoh penggunaan
golongan = 'c'
jam_kerja = 40
jam_lembur = 10

upah_total = hitung_upah(golongan, jam_kerja, jam_lembur)
print(f"Upah total untuk golongan {golongan}, {jam_kerja} jam kerja dan {jam_lembur} jam lembur: Rp {upah_total}")
