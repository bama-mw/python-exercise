import os
os.system ("cls")

USERNAME = 'bama2262@gmail.com'
PASSWORD = '2262'

username = input("Masukan Username: ")
password = input("Masukan Password: ")

if username != USERNAME:
    print("Username Tidak Tersedia." )
elif username == USERNAME and password != PASSWORD:
    print("Password Salah!")
else :
    print("Selamat datang ",username)