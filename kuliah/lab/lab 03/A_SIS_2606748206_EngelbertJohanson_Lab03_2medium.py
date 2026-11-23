# input
n = int(input('Masukkan jumlah kucing: '))
sisa_nasi = int(input('Masukkan sisa nasi (suap): '))

    # perulangan setiap kucing
for i in range (1,n+1,1) :
    level = int(input(f'Masukkan level kelaparan kucing ke-{i}:'))

    # Tentukan berapa suap yang dibutuhkan
    if level > 6:
        suap = 3
    elif 3 <= level <= 6:
        suap = 1
    else:
        suap = 0
    
    # Cek apakah nasi cukup
    if sisa_nasi < suap:
        print(f"Kucing {i}: nasi gak cukup, kabur!")
        break  # Hentikan program seketika
    
    # Jika cukup, kurangi sisa nasi dan cetak status
    if suap > 0:
        sisa_nasi -= suap
        print(f"Kucing {i}: dikasih {suap} suap. Sisa nasi: {sisa_nasi}")
    else:
        print(f"Kucing {i}: gak dikasih. Sisa nasi: {sisa_nasi}")
