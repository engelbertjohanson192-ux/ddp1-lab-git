# TODO 1: Buka file sensor_mentah.txt agar isinya dapat dibaca oleh program.
# Siapkan sebuah variabel penghitung (inisialisasi dengan nilai 0) untuk melacak 
# berapa banyak baris data cuaca yang bernilai valid dan berhasil direkap.

file_input = open('sensor_mentah.txt','r')
file_output = open('cuaca_rapi.txt', 'w+')
file_error = open('error.log', 'a')
count_valid = 0
CHM='CHMchm'
new_cuaca_1=''

pemisah = "|"


# TODO 2: Lakukan perulangan untuk membaca data dari file teks tersebut baris demi baris.
for line in file_input:
    valid = True
    new_date = ""
    new_lokasi = ""

    # Pada setiap barisnya, pisahkan data menjadi tiga komponen: Tanggal, Lokasi, dan Log Cuaca. 
    # Pemisahan dilakukan berdasarkan karakter pembatas pipa ( | ).
    # Bersihkan setiap komponen data dari spasi kosong atau karakter baris baru (newline) yang menempel 
    # di awal maupun akhir kata.Sesuaikan format teks pada komponen Lokasi agar setiap awal katanya 
    # menggunakan huruf kapital (Title Case).
    # HINT: Gunakan method find() dan string slicing.
    line_clean = line.strip()
    if not line_clean:
        continue

    clean1 = line_clean.find('|')
    clean2 = line_clean.find('|', clean1 + 1)

    date = line_clean[0:clean1].strip()
    lokasi = line_clean[clean1 + 1:clean2].strip()
    cuaca = line_clean[clean2 + 1:].strip()

    new_lokasi = lokasi.title()

    # TODO 3: Format Tanggal pada data mentah adalah YYYY-MM-DD (contoh: 2026-10-12).
    # Pecah komponen tanggal tersebut, lalu susun ulang urutannya agar menjadi format kalender standar, 
    # yaitu DD/MM/YYYY (contoh: 12/10/2026).
    # HINT: Mirip dengan todo sebelumnya, gunakan find() dan string slicing.

   
    cari1 = date.find('-')
    cari2 = date.find('-', cari1 + 1)

    year = date[0:cari2]
    month = date[cari1 + 1:cari2]
    day = date[cari2 + 1:]
    new_date = day + "/" + month + "/" + year

    # TODO 4: Lakukan pengecekan terhadap komponen Log Cuaca untuk mendeteksi data yang rusak. 
    # Data dianggap rusak jika terdapat karakter selain huruf “C”, “H”, atau “M” di dalam deretannya.
    valid = True
    for log_cuaca in cuaca :
        if log_cuaca not in CHM:
            valid = False

    # TODO 5: Jika data valid (tidak rusak): Lakukan kompresi Run-Length Encoding pada rentetan huruf di Log Cuaca.
    counter = 1
    new_cuaca = []
    if valid and len(cuaca) > 0:
        for x in range (1, len(cuaca)):
            if cuaca[x] == cuaca[x - 1] :
                counter += 1
            else :
                new_cuaca.append(f'{counter}{cuaca[x - 1]}')
                counter = 1
                
        new_cuaca.append(f"{counter}{cuaca[-1]}")
        
            
        new_cuaca_1 = "".join(new_cuaca)
        
        file_output.write(f"{new_date} - {new_lokasi}: {new_cuaca_1}\n")
        count_valid += 1

    # Jika data rusak (tidak valid): Hentikan pemrosesan untuk baris ini. Catat laporan kerusakan ke 
    # dalam file baru bernama error.log (pastikan menggunakan mode penambahan/append agar 
    # data sebelumnya tidak tertimpa).
    # Format log error: "Data rusak pada [Tanggal Baru] di [Lokasi] dengan log cuaca [Log Cuaca].'
    # Note: [Tanggal Baru] merupakan tanggal yang urutannya telah disusun ulang menjadi DD/MM/YYYY.
    else:
        file_error.write(f"Data rusak pada {new_date} di {new_lokasi} dengan log cuaca {cuaca}\n")


# TODO 6: Setelah perulangan selesai, cetak ke layar terminal total data yang berhasil diproses secara valid.
# Pastikan semua file yang telah kamu buka selama berjalannya program ditutup dengan benar untuk 
# menghindari kebocoran memori.
print(f'Total data valid :{count_valid}')

file_output.close()
file_error.close()
file_input.close()


#jangan diilangkan