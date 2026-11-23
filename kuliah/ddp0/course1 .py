import math

# TODO: Input
waktu = int(input('waktu berputar dalam menit : '))
pusat_x = int(input('kordinat x : '))
pusat_y = int(input('kordinay y : '))
jari_jari = int(input ('jari-jari dalam meter : '))
sudut_awal = int(input('sudut kabin saat ni dalam derajat : '))

# TODO: Hitung sudut
x = jari_jari * math.cos(math.radians(sudut_awal+waktu*6))
y = jari_jari * math.sin(math.radians(sudut_awal+waktu*6))
# TODO: Hitung koordinat akhir
x_akhir = pusat_x + x
y_akhir = pusat_y + y

# Output
print(f"{x_akhir:.2f}, {y_akhir:.2f}")