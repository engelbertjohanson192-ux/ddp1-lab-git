print('=====================================')
print('SISTEM PENGIRIMAN PAKET')
print('=====================================')

# bagian input

jenis_layanan = input('Masukkan jenis layanan (reguler/express/same_day): ')
# rumus tarif_per_kg
if (jenis_layanan == 'reguler') :
    tarif_per_kg = 4000
elif (jenis_layanan == 'express') :
    tarif_per_kg = 7000
elif (jenis_layanan == 'same_day') :
    tarif_per_kg = 10000
else :
    exit(
        print('''
=====================================
Jenis layanan tidak dikenali.
=====================================
            ''')
        )
    
berat_paket = int(input('Masukkan berat paket (kg): '))

pecah_belah = input('Apakah paket pecah belah? (ya/tidak): ')
# biaya penanganan
if (pecah_belah == 'ya') :
    biaya_penanganan = 8000
elif (pecah_belah == 'tidak') :
    biaya_penanganan = 0
else :
    exit(
        print('''
=====================================
Jenis pecah_belah tidak dikenali.
=====================================
            ''')
        )


anggota = input('Apakah pelanggan merupakan anggota? (ya/tidak): ')
# perhitungan berat 
biaya_dasar = berat_paket * tarif_per_kg
# diskon_anggot
if (anggota == 'ya') :
    diskon = biaya_dasar*0.2
elif (anggota == 'tidak') :
    diskon = 0
else :
    exit(
        print('''
=====================================
Jenis anggota tidak dikenali.
=====================================
            ''')
        )

metode_pembayaran = input('Masukkan metode pembayaran (tunai/saldo): ')
# untuk pembayaran dengan saldo 
if (metode_pembayaran == 'saldo') :
    saldo = int(input('Masukkan saldo: '))
elif(metode_pembayaran == 'tunai') : 
    pass
else :
    exit(
            print('''
=====================================
Jenis metode_pembayaran tidak dikenali.
=====================================
                ''')
            )
print('')
print('========== RINCIAN PENGIRIMAN ==========')

# batas_diskon
if(diskon >= 15000) :
    diskon = 15000
    
#total_biaya
total_biaya = biaya_dasar - diskon + biaya_penanganan
total_biaya=int(total_biaya)
# output
print(f'Biaya dasar          : Rp {biaya_dasar}')
print(f'Diskon anggota       : Rp {int(diskon)}')
print(f'Biaya penanganan     : Rp {biaya_penanganan}')

print('-----------------------------------------')
if (metode_pembayaran == 'saldo'):
    print(f'Total biaya          : Rp {total_biaya}')
    sisa_saldo = saldo - total_biaya
    if (sisa_saldo < 0) :
        print('Saldo tidak mencukupi!')
        kurang_saldo = -(sisa_saldo)
        print(f'Kekurangan saldo     : Rp {kurang_saldo}')
    elif (sisa_saldo >= 0) :
        print(f'Sisa saldo           : Rp {sisa_saldo}')
elif (metode_pembayaran == 'tunai') : 
    print(f'Total biaya          : Rp {total_biaya}')
    print('Pembayaran dilakukan secara tunai.')
print('=====================================')
