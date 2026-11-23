class MataKuliah:
    def __init__(self, kode, nama, sks):
        # TODO 1:
        # Simpan kode, nama, dan sks sebagai atribut objek.
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def hitung_durasi(self):
        # TODO 2:
        # Hitung dan kembalikan durasi perkuliahan.
        return self.sks*50

    def tampilkan_info(self):
        # TODO 3:
        # Cetak seluruh informasi mata kuliah sesuai format.
        print(f'Kode: {self.kode}')
        print(f'Nama: {self.nama}')
        print(f'Jumlah SKS: {self.sks}')
        print(f'Durasi Perkuliahan: {self.hitung_durasi()} menit')


print("=== INFORMASI MATA KULIAH ===")
kode = input("Masukkan kode mata kuliah: ")
nama = input("Masukkan nama mata kuliah: ")
sks = int(input("Masukkan jumlah SKS: "))

# TODO 4:
# Buat objek MataKuliah dan tampilkan informasinya.
mata_kuliah = MataKuliah(kode,nama,sks)

print('=== RINCIAN MATA KULIAH ===')
mata_kuliah.tampilkan_info()


