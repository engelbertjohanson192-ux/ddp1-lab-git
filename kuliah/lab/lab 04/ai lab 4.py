# =====================================================================
# Nama  : Engelbert Johanson
# NPM   : 2606748206
# Kelas : A
# =====================================================================
# Kerjakan setiap TODO di bawah sesuai dengan spesifikasi soal Lab 04.
# =====================================================================

print("=== POUPET SIMULATOR ===")

# Inisialisasi status awal PouPet
kenyang = 40
mood = 40
vokal = 'aiueo'
konsonan = 'bcdfghjklmnpqrstvwxyz'
alfabet = vokal + konsonan

# Loop utama
while True:
    makanan = input("Beri makan PouPet: ")

    # TODO 1: Cek apakah input adalah kata "TIDUR".
    if makanan == 'TIDUR':
        print('Poupet tertidur pulas... Sampai jumpa!')
        break

    makanan = makanan.lower()
    makanan_bersih = ""

    # TODO 2 & TODO 3: Hitung efek status dan bersihkan string makanan
    for poin in makanan:
        if poin in vokal:
            kenyang += 5
            makanan_bersih += poin.upper()
        elif poin in konsonan:
            mood += 3
            makanan_bersih += poin.lower()
        else:
            # Non-alfabet (termasuk spasi dan simbol)
            kenyang -= 5
            mood -= 5

    # TODO 4: Cetak status makanan di piring
    if len(makanan_bersih) == 0:
        print("Makanan di piring: (piring kosong, semua dibuang)")
    else:
        print(f"Makanan di piring: {makanan_bersih}")

    # TODO 5: Cek kemunculan huruf alfabet yang sama secara berurutan minimal 3 kali
    count = 1
    berulang = False
    for poin in range(1, len(makanan_bersih)):
        if makanan_bersih[poin] == makanan_bersih[poin-1]:
            count += 1
            if count >= 3:
                berulang = True
                break
        else:
            count = 1
    
    if berulang:
        mood -= 15
        print('Huwek! Terlalu banyak huruf berulang')

    # TODO 6: Cek apakah string bersih merupakan palindrom (panjang minimal 2 karakter)
    polindrom = ""
    for poin in makanan_bersih:
        polindrom = poin + polindrom
    
    if len(makanan_bersih) >= 2 and polindrom == makanan_bersih:
        mood += 20
        print(f"NYAM! Palindrom {makanan_bersih} lezat!")

    # Membatasi nilai kenyang dan mood agar tetap di rentang 0 - 100
    if kenyang > 100:
        kenyang = 100
    elif kenyang < 0:
        kenyang = 0

    if mood > 100:
        mood = 100
    elif mood < 0:
        mood = 0    

    # TODO 7: Cetak progress bar dan nilai status terbaru untuk kenyang dan mood
    bar_kenyang = "#"
    bar_mood = "#"
    strip = '-'
    peng_kali_kenyang = kenyang // 10
    peng_kali_mood = mood // 10
    print(f"Kenyang: [{bar_kenyang * peng_kali_kenyang + strip * (10 - peng_kali_kenyang)}] {kenyang}/100 | Mood: [{bar_mood * peng_kali_mood + strip * (10 - peng_kali_mood)}] {mood}/100")
    
    # Cek kondisi Game Over
    if kenyang <= 0 and mood <= 0:
        print("Game Over! PouPet kelaparan dan marah")
        break
    elif kenyang <= 0:
        print("Game Over! PouPet kelaparan")
        break
    elif mood <= 0:
        print("Game Over! PouPet marah")
        break