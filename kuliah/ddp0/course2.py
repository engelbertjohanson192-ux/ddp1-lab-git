import math

# TODO: Input awal program
T0 = float(input('masukan suhu awal air : '))
d = float(input('perubahan suhu setiap menit : '))
n = input('maksimal waktu pengamatan : ')

# TODO: Lakukan perulangan untuk setiap menit
for t in range (0,int(n)+1):


# TODO: Hitung suhu air dan lakukan pembulatan hasilnya
    Tt=T0-(d*float(t))
    

# TODO: Periksa apakah suhu sudah di bawah 30°C dan berikan output pesan yang sesuai
    if(Tt>30):
        print(f't = {t},  suhu = {math.floor(Tt)}')
    else : 
        print(f't = {t},  suhu = {math.floor(Tt)} (air sudah mendidih)')
        break