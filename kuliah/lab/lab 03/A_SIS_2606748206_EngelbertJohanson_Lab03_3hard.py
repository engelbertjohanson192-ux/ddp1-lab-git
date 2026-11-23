# =======================================================
# Program 3 (Hard) - Sesi Siang: Kakak Asdos Doom Scrolling
# =======================================================

# 1. Input awal
fokus = int(input("Masukkan level fokus awal: "))
jumlah_konten = int(input("Masukkan jumlah konten yang di-scroll: "))

# Variabel bantuan untuk menghitung konten berat (kode 2) berturut-turut
beruntun_berat = 0

# =======================================================
# TODO: Buat pengulangan (loop) sebanyak jumlah_konten di bawah ini!
# =======================================================
for i in range(1, jumlah_konten + 1):
    kode = int(input(f"Masukkan kode konten ke-{i} (1/2/3): "))
    
    # Process kode konten
    if kode == 1:
        fokus -= 5
        beruntun_berat = 0
    elif kode == 2:
        fokus -= 15
        beruntun_berat += 1
    elif kode == 3:
        fokus += 20
        beruntun_berat = 0
    else : 
        exit (
            print ('''
            ====================
            kode tidak valid
            ====================
            ''')
        )
    
    # Cek & clamp batas fokus setelah perubahan dari kode
    if fokus > 100:
        fokus = 100
    elif fokus < 0:
        fokus = 0

    # Cek penalti brain rot
    if beruntun_berat == 2:
        fokus -= 10
        beruntun_berat = 0
        
        # Cek & clamp batas fokus setelah penalti brain rot
        if fokus > 100:
            fokus = 100
        elif fokus < 0:
            fokus = 0

# =======================================================
# TODO: Tentukan status akhir berdasarkan nilai 'fokus'
# =======================================================
if fokus == 0:
    status = "Otak Kosong"
elif 0 < fokus < 20:
    status = "Butuh Healing"
else:
    status = "Masih Waras"

# 2. Cetak output akhir sesuai format
print(f"Fokus akhir: {fokus}")
print(f"Status: {status}")