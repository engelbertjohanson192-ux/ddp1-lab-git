# TODO: import library yang diperlukan
import math

print("=" * 60)
print("SELAMAT DATANG DI SISTEM PENCATATAN PENDUDUK FLORIAN!")
print("=" * 60)

print("\n==== Data Penduduk ====")

# TODO: lengkapi input-input di bawah ini
nama = input ('nama : ')
tempat_lahir = input ('tempat lahir : ')
tanggal_lahir = input ('tanggal lahir : ')
spesies = input ('spesies : ')
tinggi = input ('tinggi (dalam m): ')
berat = input ('berat (dalam kg) : ')

# TODO: hitung tinggi dan luas rumah
# refer kembali ke rumus yang disediakan pada soal
tinggi_rumah = float(tinggi)+ 0.85
luas_rumah = math.pi * math.sqrt(2)*(float(tinggi)**2)+(float(berat)/3)

# TODO: tampilkan luaran sesuai dengan test case yang ada pada dokumen soal
# ingat bahwa bilangan dibulatkan dua angka di belakang koma
print(f'\n Penduduk berspesies {spesies} dengan nama {nama} \n yang lahir tanggal {tanggal_lahir} di {tempat_lahir} berhasil terdaftar \n menjadi penduduk negeri Florian!')
print(f'\n {nama}berhak atas rumah dengan tinggi {round(tinggi_rumah,2)} meter dan \n luas {round(luas_rumah,2)} meter persegi.')

print("=" * 60)
print("TERIMA KASIH SUDAH MELAKUKAN PENCATATAN DATA PENDUDUK!")
print("=" * 60)
