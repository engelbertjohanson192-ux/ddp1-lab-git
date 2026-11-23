# =====================================================================
# Nama  :
# NPM   :
# Kelas :
# =====================================================================
# Perbaiki error yang muncul dan kerjakan setiap TODO di bawah.
# =====================================================================

LEBAR = 30

# --- Bagian input ----------------------------------------------------
nama = input("Masukkan nama lengkap: ")
npm = int(input("Masukkan NPM: "))
kelas = input( "Masukan kelas: ")

# TODO 1: tambahkan satu baris untuk meminta input kelas dari pengguna
#         dengan prompt "Masukkan kelas: " dan simpan ke variabel kelas.


# --- Bagian output ---------------------------------------------------
print("=" * LEBAR)
print("  KARTU MAHASISWA FASILKOM  ")
print("=" * LEBAR)
print("Nama     : " + nama)
print("NPM      : " + str(npm))
print("Kelas    : " + kelas)
print('Fakultas : Ilmu Komputer')
# TODO 2: cetak satu baris berisi "Fakultas : Ilmu Komputer"

print("=" * LEBAR)

# soal bonus 
print("=" * LEBAR)
print(  '~SOAL BONUS~')
print("=" * LEBAR)


# input 
hobi = input("Masukkan hobi anda: ")
quote = input("Masukkan quote penyemangat: ")
github = input( "Masukan web github: ")

# output
print("=" * LEBAR)
print("  KARTU MAHASISWA FASILKOM  ")
print("         - SISI BELAKANG -")
print("=" * LEBAR)
print('Hobi     :'+ hobi)
print('Quote    :'+ quote)
print('GitHub   :'+ github)
print("=" * LEBAR)
