# =====================================================================
# Nama  :Engelbert Johanson
# NPM   :2606748206
# Kelas :A
# =====================================================================
# Kerjakan setiap TODO di bawah sesuai dengan spesifikasi soal Lab 04.
# =====================================================================

print("=== POUPET SIMULATOR ===")

# Inisialisasi status awal PouPet
kenyang = 40
mood = 40
vokal = 'aiueo'
konsonan = 'bcdfghjklmnpqrstvwxyz'
makanan_bersih = ""
alfabet = vokal + konsonan
polindrom =''
ban = 0

# Loop utama
while True:
    makanan = input("Beri makan PouPet: ")

    # TODO 1: Cek apakah input adalah kata "TIDUR".
    #         Jika ya, cetak "Poupet tertidur pulas... Sampai jumpa!"
    #         lalu hentikan perulangan (break).
    
    if (makanan == 'TIDUR') :
        print ('Poupet tertidur pulas... Sampai jumpa!')
        break

    makanan = makanan.lower()

    # TODO 2: Hitung efek setiap karakter terhadap status kenyang dan mood:
    #          - Huruf vokal: kenyang +5 poin
    #          - Huruf konsonan: mood +3 poin
    #          - Non-alfabet (termasuk spasi): kenyang -5 poin dan mood -5 poin


    
    # TODO 3: Lakukan pembersihan makanan ke dalam variabel penampung string bersih:
    #          - Huruf vokal diubah menjadi huruf kapital
    #          - Huruf konsonan diubah menjadi huruf kecil
    #          - Non-alfabet (termasuk spasi) dibuang


    # HINT: TODO 2 dan TODO 3 dapat digabung dalam satu perulangan (loop)
    #       yang sama karena logika pengecekan jenis karakternya identik.

    for poin in makanan :
        if poin in vokal :
            kenyang +=5
            makanan_bersih = makanan_bersih + poin.upper()
        elif poin in konsonan :
            mood +=3
            makanan_bersih = makanan_bersih + poin.lower()
        elif poin not in konsonan and vokal :
            kenyang -= 5
            mood -= 5

    # TODO 4: Cetak status makanan di piring:
    #         - Jika string bersih kosong:
    #           "Makanan di piring: (piring kosong, semua dibuang)"
    #         - Jika tidak kosong:
    #           "Makanan di piring: [string bersih]"
    
    for poin in makanan_bersih :
        if poin.lower() not in alfabet :
            print ("Makanan di piring: (piring kosong, semua dibuang)")
            break
        else :
            print(f'Makanan di piring: {makanan_bersih}')
            break
    # TODO 5: Cek kemunculan huruf alfabet yang sama secara berurutan minimal 3 kali
    #         pada nama makanan yang sudah dibersihkan.
    #         Jika terdeteksi, kurangi mood sebanyak 15 poin dan cetak:
    #         "Huwek! Terlalu banyak huruf berulang"
    # HINT: Lakukan perulangan dengan variabel penghitung berurutan,
    #       lalu segera 'break' saat hitungan mencapai 3.      
    
    count = 1
    berulang = False
    for poin in range(1,len(makanan_bersih)) :
        if makanan_bersih[poin] == makanan_bersih[poin-1]:
            count +=1
            if (count >= 3):
                berulang=True
                break
        else :
            count = 1
    
    if berulang == True   :
        mood -=15
        print ('Huwek! Terlalu banyak huruf berulang')
                      

    # TODO 6: Cek apakah string bersih merupakan palindrom (panjang minimal 2 karakter).
    #         Bentuk string terbalik menggunakan perulangan (dilarang menggunakan [::-1]).
    #         Jika palindrom, tambah mood sebanyak 20 poin dan cetak:
    #         "NYAM! Palindrom [string bersih] lezat!"
    # HINT: Karena dilarang menggunakan slicing [::-1], bisa susun string terbalik secara manual
    #       melalui loop dengan pola `terbalik = char + terbalik`, lalu bandingkan jika panjang string minimal 2.

    for poin in makanan_bersih :
        polindrom = poin + polindrom
    
    if polindrom == makanan_bersih :
        mood +=20
    
    if kenyang > 100:
        kenyang = 100
    elif kenyang < 0:
        kenyang = 0

    if mood > 100:
        mood = 100
    elif mood < 0:
        mood = 0    


    # TODO 7: Cetak progress bar dan nilai status terbaru untuk kenyang dan mood.
    #         Format: "Kenyang: [####------] [kenyang]/100 | Mood: [####------] [mood]/100"
    # HINT: Manfaatkan operator perkalian string untuk membuat progress bar.
    bar_kenyang = "#"
    bar_mood = "#"
    strip = '-'
    peng_kali_kenyang = kenyang // 10
    peng_kali_mood = mood // 10
    print(f"Kenyang: [{bar_kenyang*peng_kali_kenyang+strip*(10-peng_kali_kenyang)}] {kenyang}/100 | Mood: [{bar_mood*peng_kali_mood+strip*(10-peng_kali_mood)}] {mood}/100")
    makanan_bersih =''
    
    if kenyang <= 0 and mood <= 0:
        print("Game Over! PouPet kelaparan dan marah")
        break
    elif kenyang <= 0:
        print("Game Over! PouPet kelaparan")
        break
    elif mood <= 0:
        print("Game Over! PouPet marah")
        break