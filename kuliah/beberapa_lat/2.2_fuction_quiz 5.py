def is_email_valid(email):
    # Mengembalikan True jika karakter '@' tepat berjumlah 1
    return email.count('@') == 1


nama_file = input('Nama file : ')

try:
    with open(nama_file, 'r') as my_file:
        counter_invalid = 0
        for line in my_file:
            # Panggil fungsi is_email_valid
            if not is_email_valid(line):
                counter_invalid += 1
                
        print(f'Terdapat {counter_invalid} email tidak valid')

except FileNotFoundError: 
    print('File tidak ditemukan')