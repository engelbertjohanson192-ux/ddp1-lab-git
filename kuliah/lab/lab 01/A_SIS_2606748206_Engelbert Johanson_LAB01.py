# =====================================================================
# Nama  : Engelbert Johanson
# NPM   : 2606748206
# Kelas : A
# =====================================================================
# Perbaiki error yang muncul dan kerjakan setiap TODO di bawah.
# =====================================================================

print("======================================== ")
print("        WELCOME TO PACIL LIBRARY ")
print("======================================== ")

# --- Bagian input ------------------------------------------------------
judul_buku = input("Masukkan judul buku: ")
jumlah_buku = int(input("Masukkan jumlah buku yang ingin dipinjam: "))
harga_sewa = int(input("Masukkan harga sewa per buku (rupiah): "))
diskon = float(input('Masukan diskon (%): '))
nama_bank = input('Masukan nama bank pembayaran: ')
saldo_awal = int(input('Masukan saldo awal (rupiah): '))
durasi_peminjaman = int(input('Masukan durasi peminjaman (hari): '))

# TODO 1: Tambahkan beberapa input dan simpan hasilnya ke dalam variabel
#         diskon, nama_bank, saldo_awal, dan durasi_peminjaman. Gunakan
#         tipe data yang sesuai untuk setiap input, seperti yang diminta
#         pada spesifikasi program.


# --- Bagian proses -------------------------------------------------------
# TODO 2: Konversi durasi_peminjaman (dalam hari) menjadi minggu dan hari.
#         Simpan jumlah minggu ke variabel minggu, dan sisa hari ke
#         variabel hari.
# Keterangan: manfaatkan operator pembagian bulat (//) untuk mendapatkan
#             jumlah minggu, dan operator modulo (%) untuk mendapatkan
#             sisa hari.
minggu = str(durasi_peminjaman//7)
hari = str(durasi_peminjaman%7)


# TODO 3: Bentuk variabel kode_peminjaman dengan menggabungkan judul_buku,
#         jumlah_buku, dan nama_bank
kode_peminjaman = str(judul_buku+str(jumlah_buku)+nama_bank)


subtotal = float(harga_sewa * jumlah_buku)

# TODO 4: Hitung nominal_diskon, yaitu persentase diskon dikali subtotal,
#         lalu dibagi 100. Simpan ke variabel nominal_diskon.
nominal_diskon = float(subtotal * diskon / 100)


# TODO 5: Hitung total_bayar, yaitu subtotal dikurangi nominal_diskon.
#         Simpan ke variabel total_bayar.
total_bayar = float(subtotal - nominal_diskon)


sisa_saldo = float(saldo_awal - total_bayar)


# --- Bagian output ---------------------------------------------------
print("======================================== ")
print("              RENTAL SUMMARY ")
print("======================================== ")
print("----------- DETAIL PEMINJAMAN ----------- ")
print("Buku : " + judul_buku)
print("Durasi Peminjaman : " + str(minggu) + " minggu " + str(hari) + " hari")
print("Kode Peminjaman : " + kode_peminjaman)
print("----------- DETAIL PEMBAYARAN ----------- ")
# TODO 6: Tampilkan subtotal, nominal diskon, total pembayaran, dan sisa saldo
#         menggunakan format output yang sesuai dengan contoh pada spesifikasi
#         program.
print(f'Subtotal : Rp{subtotal}')
print(f'Diskon ({int(diskon)}%) : Rp{nominal_diskon}')
print(f'Ttotal Pembbayaran : Rp{total_bayar}')
print(f'Sisa Saldo {nama_bank} Anda : Rp{sisa_saldo}')
