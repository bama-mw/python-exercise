# Baca karakter
char = input("Masukkan karakter: ")

# Periksa apakah karakter adalah digit
if char.isdigit():
    nilai_integer = ord(char) - ord('0')
else:
    nilai_integer = -99

# Tampilkan hasil
print("Nilai integer:", nilai_integer)
