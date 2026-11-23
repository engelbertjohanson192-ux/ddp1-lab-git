def matkul_diambil(mk):
    """
    Mengembalikan list MK yang dapat diambil semester depan
    sebagai langkah menuju mk.

    Variabel yang dapat digunakan:
    - lulus     : list kode MK yang sudah lulus
    - prasyarat : dictionary {kode MK: list kode prasyaratnya}
                  MK tanpa prasyarat tidak ada di dictionary ini.
    """
    # TODO 1:
    # Tangani kondisi ketika mk sudah lulus.
    ...

    # TODO 2:
    # Kumpulkan MK yang dapat diambil semester depan
    # dari setiap prasyarat mk.
    hasil = []
    for p in ...:
        ...

    # TODO 3:
    # Jika tidak ada MK yang perlu diambil lebih dulu,
    # mk sendiri dapat diambil semester depan.
    if ...:
        ...

    # TODO 4:
    # Jika tidak, kembalikan MK yang dikumpulkan di TODO 2.
    ...


# ===== Program utama =====
target = input()
lulus = input().split()
prasyarat = {}

# TODO 5:
# Baca M, lalu simpan M baris data prasyarat ke dictionary prasyarat.
# Kata pertama tiap baris menjadi key, sisanya menjadi value.
m = ...
...

# TODO 6:
# Panggil matkul_diambil(target), buang MK yang muncul lebih dari sekali,
# urutkan secara abjad, lalu cetak sesuai format output.
hasil = ...
...