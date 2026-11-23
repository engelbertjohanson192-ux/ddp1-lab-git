def hitung_cara(sisa_blok, sebelumnya_dua):
    jumlah_cara=1
    trial = 0
    # TODO 1:
    # Tangani kondisi ketika seluruh blok berhasil dicadangkan
    # dan ketika proses mengambil terlalu banyak blok.
    if sisa_blok < 0 :
        return 0
    if sisa_blok == 0 :
        return 1

    # TODO 2:
    # Hitung banyak cara jika proses berikutnya mencadangkan satu blok.
    jumlah_cara = hitung_cara(sisa_blok-1, False)
    

    # TODO 3:
    # Jika diperbolehkan, tambahkan kemungkinan mencadangkan dua blok.
    if sebelumnya_dua == False:
        jumlah_cara +=  hitung_cara(sisa_blok-2,True)
        
        

    # TODO 4:
    # Kembalikan jumlah seluruh cara yang valid.
    return jumlah_cara


print("=== SISTEM PENCADANGAN DATA AKADEMIK ===")
n = int(input("Masukkan jumlah blok data: "))

hasil = hitung_cara(n, False)

print("\n=== HASIL ANALISIS ===")
print(f"Untuk {n} blok data, terdapat {hasil} cara pencadangan yang valid.")