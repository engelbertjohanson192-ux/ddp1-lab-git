# Header
print("============================================================")
print("SISTEM PENCATATAN ANGGOTA KDMP FLORIAN")
print("============================================================")


def tentukan_paket(skor_usaha):
    # TODO: Menentukan paket berdasarkan skor usaha
    if (int(skor_usaha)<50 and int(skor_usaha)>=0):
        return "Paket Tunas"
    elif (int(skor_usaha)<80 and int(skor_usaha)>49):
        return "Paket Mekar"
    else:
        return "Paket Mandiri"


# TODO: Meminta banyak anggota yang akan didaftarkan
daftar_anggota = []
banyak_anggota = input('Masukan banyak anggota : ')

# TODO: Meminta data untuk setiap anggota
for nomor in range(1, int(banyak_anggota)+1 ):
    print(f"\n=== Data anggota {nomor} ===")
    # TODO: Mengambil input
    nama = input('Nama anggota : ')
    kode_wilayah = input('Cabang KDMP (G/L/P) : ')
    skor_usaha = input('Skor usaha : ')
    komoditas = input('Komoditas ungguan : ')

    # TODO: Mengubah kode wilayah menjadi nama wilayah
    if (kode_wilayah=='G'):
        wilayah = "Pegunungan"
    elif (kode_wilayah=='L'):
        wilayah = "Lembah"
    else:
        wilayah = "Pesisir"

    paket = tentukan_paket(skor_usaha)

    # Data anggota disimpan sebagai tuple dengan urutan:
    # Nama, Wilayah, Skor Usaha, Komoditas, Paket
    data_anggota = (nama, wilayah, skor_usaha, komoditas, paket)
    daftar_anggota.append(data_anggota)


# TODO: Menampilkan data anggota dalam bentuk tabel
jumlah_tunas = 0
jumlah_mekar = 0
jumlah_mandiri = 0

print("\n====================== DATA ANGGOTA KDMP ======================")
print(f"{'No':<3} {'Nama':<12} {'Wilayah':<11} {'Skor':>4} {'Komoditas':<12} {'Paket':<14}")

for i in range(int(banyak_anggota)):
    anggota = daftar_anggota[i]
    nama, wilayah, skor_usaha, komoditas, paket = anggota

    print(f"{i+1:<3} {nama:<12} {wilayah:<11} {skor_usaha:>4} {komoditas:<12} {paket:<14}")

    # TODO: Menghitung jumlah anggota pada setiap paket
    if (int(skor_usaha)<50 and int(skor_usaha)>=0):
        jumlah_tunas += 1
    elif (int(skor_usaha)<80 and int(skor_usaha)>49):
        jumlah_mekar += 1
    else:
        jumlah_mandiri += 1


print("====================== RINGKASAN KDMP ======================")
print(f"Jumlah penerima Paket Tunas: {jumlah_tunas}")
print(f"Jumlah penerima Paket Mekar: {jumlah_mekar}")
print(f"Jumlah penerima Paket Mandiri: {jumlah_mandiri}")

# BONUS: uncomment dan lengkapi jika mengerjakan bonus
# def tampilkan_anggota_per_paket(daftar_anggota):
def tampilkan_anggota_per_paket(daftar_anggota):
    print("\n====================== DAFTAR ANGGOTA PER PAKET ======================")

    tunas = []
    mekar = []
    mandiri = []

    for anggota in daftar_anggota:
        nama, wilayah, skor_usaha, komoditas, paket = anggota

        if paket == "Paket Tunas":
            tunas.append(nama)
        elif paket == "Paket Mekar":
            mekar.append(nama)
        elif paket == "Paket Mandiri":
            mandiri.append(nama)

    print(f"Paket Tunas: {', '.join(tunas) if tunas else '-'}")
    print(f"Paket Mekar: {', '.join(mekar) if mekar else '-'}")
    print(f"Paket Mandiri: {', '.join(mandiri) if mandiri else '-'}")

      
# tampilkan_anggota_per_paket(daftar_anggota)
tampilkan_anggota_per_paket(daftar_anggota)

print("============================================================")
print("TERIMA KASIH SUDAH MEMBANTU KDMP FLORIAN!")
print("============================================================")