
# soal 1
def uji_coba (nama,huruf):
    nama=nama.upper()
    huruf=huruf.upper()
    return print(nama.count(huruf))

uji_coba('DDP-1-d','D')

# soal 2
def no2 (name) :
    spasi = ' '
    inisial = ''
    while True:
        if spasi in name:
            cari_1 = name.find(spasi)
            inisial=inisial+name[0:1:]
            name=name[cari_1+1::]
        else :
            inisial=inisial+name[0:1:]
            break
    return print(inisial.upper())

no2('Lulu angelic Man')

# solusi lainnya untuk no2 
def initial (kode):
    hasil=''
    kata_baru=True
    for huruf in kode:
        if huruf != " ":
            if kata_baru:
                hasil+=huruf.upper()
                kata_baru=False
        else:
            kata_baru=True
    return print(hasil)

initial('Lulu ilmaknun gunrum')