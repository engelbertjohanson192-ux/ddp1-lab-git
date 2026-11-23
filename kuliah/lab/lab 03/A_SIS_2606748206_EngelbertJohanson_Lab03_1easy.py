# input 
nama = input('Masukan nama Asdos: ')
kode_asdos = ''
vokal = "AIUEO "


for huruf in nama:
    if huruf not in vokal :
        kode_asdos = kode_asdos + huruf
    if (len(kode_asdos) == 4) :
        break
print (kode_asdos)
