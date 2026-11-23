class Lagu:
    """Representasi lagu pada aplikasi Pacil Music."""
    
    def __init__(self, judul, penyanyi, genre):
        # TODO: Lengkapi atribut.
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre
        self.disukai = False
        self.daftar_rating = []

    def __str__(self):
        # TODO Subtask 1: Implementasi method __str__().
        return f"{self.judul} - {self.penyanyi} ({self.genre})"

    def cocok_genre(self, genre):
        # TODO Subtask 2: Implementasi method cocok_genre().
        return self.genre.lower() == genre.lower()

    def buat_link(self):
        # TODO Subtask 3: Implementasi method buat_link().
        judul_link = self.judul.lower().replace(" ", "-")
        penyanyi_link = self.penyanyi.lower().replace(" ", "-")
        return (f"pacilmusic.id/{judul_link}-{penyanyi_link}")

    def toggle_like(self):
        # TODO Subtask 4: Implementasi method toggle_like().
        self.disukai = not self.disukai
        return self.disukai

    def is_disukai(self):
        # TODO Subtask 4: Implementasi method is_disukai().
        return self.disukai

    def beri_rating(self, nilai):
        # TODO Subtask 5: Implementasi method beri_rating().
        self.daftar_rating.append(nilai)

    def rata_rating(self):
        # TODO Subtask 5: Implementasi method rata_rating().
        if not self.daftar_rating:
            return 0.0
        return sum(self.daftar_rating) / len(self.daftar_rating)



# ==================== PROGRAM UTAMA ====================
def main():
    print("=== PACIL MUSIC ===")
    n = int(input("Masukkan jumlah lagu: "))

    daftar_lagu = []
    for i in range(1, n + 1):
        print(f"\nLagu ke-{i}")
        judul = input("Judul: ")
        penyanyi = input("Penyanyi: ")
        genre = input("Genre: ")
        # TODO: Buat objek Lagu dari input di atas dan masukkan ke daftar_lagu.
        daftar_lagu.append(Lagu(judul, penyanyi, genre))

    print("\n=== MENU PACIL MUSIC ===")
    print("1. Lihat daftar lagu")
    print("2. Cari lagu berdasarkan genre")
    print("3. Bagikan lagu")
    print("4. Like/unlike lagu")
    print("5. Lihat lagu yang disukai")
    print("6. Beri rating lagu")
    print("7. Lihat rata-rata rating lagu")
    print("8. Keluar")

    while True:
        menu = input("\nPilih menu: ")
        if menu == "1":
            # TODO Subtask 1: Tampilkan seluruh daftar lagu.
            for nomor, lagu in enumerate(daftar_lagu, start=1):
                print(f"{nomor}. {lagu}")

        elif menu == "2":
            # TODO Subtask 2: Minta input genre dan tampilkan nomor lagu yang cocok.
            genre_dicari = input("Genre: ")
            nomor_cocok = [
                str(nomor)
                for nomor, lagu in enumerate(daftar_lagu, start=1)
                if lagu.cocok_genre(genre_dicari)
            ]
            if nomor_cocok:
                print(f"Nomor lagu dengan genre {genre_dicari}: {', '.join(nomor_cocok)}")
            else:
                print(f"Tidak ada lagu dengan genre {genre_dicari}.")

        elif menu == "3":
            # TODO Subtask 3: Minta input nomor lagu dan tampilkan link lagu tersebut.
            nomor = int(input("Nomor lagu: "))
            print(f"Link: {daftar_lagu[nomor - 1].buat_link()}")

        elif menu == "4":
            # TODO Subtask 4: Minta input nomor lagu dan ubah status like/unlike lagu tersebut.
            nomor = int(input("Nomor lagu: "))
            if daftar_lagu[nomor - 1].toggle_like():
                print(f"Lagu nomor {nomor} ditambahkan ke Lagu yang Disukai.")
            else:
                print(f"Lagu nomor {nomor} dihapus dari Lagu yang Disukai.")

        elif menu == "5":
            # TODO Subtask 4: Tampilkan daftar nomor lagu yang disukai.
            nomor_disukai = [
                str(nomor)
                for nomor, lagu in enumerate(daftar_lagu, start=1)
                if lagu.is_disukai()
            ]
            if nomor_disukai:
                print(f"Nomor lagu yang disukai: {', '.join(nomor_disukai)}")
            else:
                print("Belum ada lagu yang disukai.")

        elif menu == "6":
            # TODO Subtask 5: Minta input nomor lagu serta nilai rating, lalu simpan rating tersebut.
            nomor = int(input("Nomor lagu: "))
            nilai = int(input("Rating (1-5): "))
            daftar_lagu[nomor - 1].beri_rating(nilai)
            print(f"Rating {nilai} untuk lagu nomor {nomor} berhasil dicatat.")

        elif menu == "7":
            # TODO Subtask 5: Minta input nomor lagu dan tampilkan rata-rata rating lagu tersebut.
            nomor = int(input("Nomor lagu: "))
            rata_rata = daftar_lagu[nomor - 1].rata_rating()
            print(f"Rata-rata rating lagu nomor {nomor}: {rata_rata:.2f}")

        elif menu == "8":
            print("Terima kasih telah menggunakan Pacil Music!")
            break

if __name__ == "__main__":
    main()











