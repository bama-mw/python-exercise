# Input: total belanja pembeli
totalBelanja = float(input("Masukkan total belanja Anda: Rp"))

# Proses: menentukan diskon dan harga setelah diskon
if totalBelanja > 100000:
    diskon = totalBelanja * 0.10
else:
    diskon = 0

hargaSetelahDiskon = totalBelanja - diskon

# Output: Menampilkan diskon dan harga setelah diskon
print(f"Diskon: Rp {diskon:,.2f}")
print(f"Harga Setelah Diskon: Rp {hargaSetelahDiskon:,.2f}")
