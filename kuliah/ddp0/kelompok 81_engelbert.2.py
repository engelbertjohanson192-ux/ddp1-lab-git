# Header 
print("============================================================")
print("KALKULATOR ANGGARAN PEMBANGUNAN INFRASTRUKTUR NEGERI FLORIAN")
print("============================================================")

# TODO: Meminta input awal
wilayah_asal = input('Masukan wilayah geografis saat ini : ')
banyak_jalan = int(input('Masukan banyak jalan yang akan dibangun : '))
sisa_anggaran = int(input('Masukan rencana anggaran pembangunan jalan : '))
biaya_per_km = int(input('Masukan biaya pembangunan jalan per kilometer : '))

# TODO: Memulai perulangan untuk setiap rute jalan
for x in range(1, banyak_jalan + 1):
    print(f"\n=== Rute jalan {x} ===")
    wilayah_tujuan = input('Wilayah geografis tujuan : ')
    panjang_jalan = input ('Panjang jalan (km) : ')
    
    # TODO: Logika percabangan untuk menentukan faktor pengali
    faktor_pengali = 1.0
    if wilayah_asal == wilayah_tujuan :
        faktor_pengali = 1.0
    elif ((wilayah_tujuan == 'G' and wilayah_asal == 'L') or (wilayah_tujuan == 'L' and wilayah_asal == 'G')):
        faktor_pengali = 1.5
    elif ((wilayah_tujuan == 'G' and wilayah_asal == 'P') or (wilayah_tujuan == 'P' and wilayah_asal == 'G')):
        faktor_pengali = 2.0
    elif ((wilayah_tujuan == 'P' and wilayah_asal == 'L') or (wilayah_tujuan == 'L' and wilayah_asal == 'P')):
        faktor_pengali = 3.0

    # TODO: Kalkulasi biaya rute dan sisa anggaran
    biaya_rute_ini = float(panjang_jalan)*biaya_per_km*faktor_pengali
    sisa_anggaran -= biaya_rute_ini
    wilayah_asal=wilayah_tujuan
    
    print(f"Biaya rute ini: {round(biaya_rute_ini)}")
    print(f"Sisa anggaran: {round(sisa_anggaran)}")

    # TODO: Kondisi jika sisa anggaran sudah bernilai negatif
    if (sisa_anggaran <= 0):
        break
    
    print("Visualisasi medan geografis:")
    # TODO: Mencetak Visualisasi Medan Geografis (BONUS)
    if (wilayah_tujuan == 'G'):
        for y in range (1, int(panjang_jalan)+1):
            print(" " * (int(panjang_jalan)-y)+ '*' * y)
    elif (wilayah_tujuan == 'L'):
        for y in range (1, int(panjang_jalan)+1):
            print(" " * (int(panjang_jalan)-y) + '*' * (2*y-1) + " " * 2*(int(panjang_jalan)-y) + '*' * (2*y-1))
    elif (wilayah_tujuan == 'P'):
        for y in range (1, int(panjang_jalan)+1):
            print('*'*y)
    

# TODO: Kondisi rencana memenuhi rancangan anggaran
print("=============================================================")
if sisa_anggaran >= 0:
    print("STATUS: RENCANA PEMBANGUNAN MEMENUHI RANCANGAN ANGGARAN")
else:
    print("STATUS: RENCANA PEMBANGUNAN TIDAK MEMENUHI RANCANGAN ANGGARAN")
print("=============================================================")