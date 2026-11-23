import random
anggota = []
nama_unik = []
TUGAS = ('Menyapu','Mengepel','Merapikan')
penjaga = {}
cadangan = []

# alur dan menu 

print ('''
 === PEMBAGIAN PIKET DEK DEPE ===
1. Tambah anggota
2. Simulasi piket
3. Rekap
4. Selesai
'''  )
# menu 1 tambah anggota
def nambah_anggota (a) :
    a.strip().lower()
    if a not in nama_unik :
        nama_unik.append(a)
        return print (f'Anggota {a} ditambahkan')
    else :
        return print (f'Anggota sudah terdaftar')
    
# menu 2 simulasi piket
def piket () :
    petugas = int(input('Jumlah petugas: '))
    ruang = int(input('Nomor ruang: '))
    jumlah_anggota = len(nama_unik)
    
    if not (1<=petugas<=jumlah_anggota) :
        print ('Jumlah petugas tidak valid')
        
    else :
        cadangan=nama_unik.copy()
    
        i=0
        
        for orang in nama_unik:
            indeks = random.randrange(len(cadangan))
            nama = cadangan.pop(indeks)
            penjaga[nama] = TUGAS[i%len(TUGAS)]
            i = i+1
        for no in range (petugas) :
            for b,c in penjaga.items() :
                print(f'{no}. {b} -> {c}') 
            return  
        
def rekap() :
    z = len(nama_unik)
    print (f'Total anggota unik ; {z}')
    print (f'Anggota : {nama_unik}')
    print ('Petugas simulasi terakhir : ')
    cadangan=nama_unik.copy()
        
    i=0
    
    for orang in nama_unik:
        indeks = random.randrange(len(cadangan))
        nama = cadangan.pop(indeks)
        penjaga[nama] = TUGAS[i%len(TUGAS)]
        i = i+1
    for no in range (len(nama_unik)) :
        for b,c in penjaga.items() :
            print(f'{no}. {b} -> {c}') 
        return  
    
            


# running 

while True :
    menu = int(input('Pilih menu: '))
    if (menu == 1 ):
        a = input('Nama Anggota: ')
        nambah_anggota(a)
    elif (menu == 2) :
        piket()
    elif (menu == 3):
        rekap()
    elif (menu == 4):
        print('Simulasi piket selesai. Sampai jumpa!')
        break
    else :
        print('Menu tidak valid.')
