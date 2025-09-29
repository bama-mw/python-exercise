# Input jumlah hari
x = int(input("Masukkan jumlah hari: "))

# Konversi ke tahun, bulan, dan hari
tahun = x // 365
sisa_hari = x % 365
bulan = sisa_hari // 30
hari = sisa_hari % 30

# Output hasil
print(f"Jumlah waktu: {tahun} tahun, {bulan} bulan, {hari} hari")
