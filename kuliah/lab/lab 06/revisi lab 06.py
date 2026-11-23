import random

# Deklarasi awal tetap dipertahankan, tipe data disesuaikan dengan spek
anggota = []
nama_unik = set() # Harus berupa set
TUGAS = ('Menyapu', 'Mengepel', 'Merapikan')
petugas = {}      # Diubah menjadi 'petugas' sesuai penamaan variabel dokumen

# Cetak satu kali di awal
print('''=== PEMBAGIAN PIKET DEK DEPE ===
1. Tambah anggota
2. Simulasi piket
3. Rekap
4. Selesai''')

# menu 1 tambah anggota
def nambah_anggota(a):
    a = a.strip().lower() # Ditampung kembali karena string immutable
    if a not in nama_unik:
        anggota.append(a) # Masukkan ke list urutan anggota
        nama_unik.add(a)  # Tambahkan ke set menggunakan add()
        print(f'Anggota {a} ditambahkan.')
    else:
        print('Anggota sudah terdaftar.')
    
# menu 2 simulasi piket
def piket():
    k = int(input('Jumlah petugas: '))
    ruang = int(input('Nomor ruang: '))
    jumlah_anggota = len(anggota)
    
    if not (1 <= k <= jumlah_anggota):
        print('Jumlah petugas tidak valid.')
    else:
        cadangan = anggota.copy()
        petugas.clear() # Kosongkan data simulasi sebelumnya
        print(f'Hasil simulasi ruang {ruang}:')
        
        for i in range(k):
            indeks = random.randrange(len(cadangan))
            nama = cadangan.pop(indeks)
            tugas = TUGAS[i % len(TUGAS)]
            
            petugas[nama] = tugas
            print(f'{i + 1}. {nama} -> {tugas}')
        
def rekap():
    z = len(nama_unik)
    print(f'Total anggota unik: {z}')
    
    if len(anggota) == 0:
        print('Anggota: -')
    else:
        # Menggabungkan list dengan koma
        print(f'Anggota: {", ".join(anggota)}') 
        
    # Mencetak simulasi terakhir tanpa diacak ulang
    if not petugas:
        print('Belum ada hasil simulasi.')
    else:
        print('Petugas simulasi terakhir:')
        for nama, tugas in petugas.items():
            print(f'{nama} -> {tugas}')

# running 
while True:
    menu = input('Pilih menu: ') # Ubah menjadi teks (str) untuk cegah ValueError
    if menu == '1':
        a = input('Nama anggota: ')
        nambah_anggota(a)
    elif menu == '2':
        piket()
    elif menu == '3':
        rekap()
    elif menu == '4':
        print('Simulasi piket selesai. Sampai jumpa!')
        break
    else:
        print('Menu tidak valid.')