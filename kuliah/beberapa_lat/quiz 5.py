nama_file = input('Nama file : ')
try:
    my_file = open(nama_file, 'r')
    counter_invalid = 0
    for line in my_file : 
        # validasi email
        if line.count('@') !=1 :
            counter_invalid += 1
    print(f'Terdapat {counter_invalid} email tidak valid')
        
except FileNotFoundError: 
    print('File tidak ditemukan')