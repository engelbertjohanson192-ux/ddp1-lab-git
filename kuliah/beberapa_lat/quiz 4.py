camelCase = input('masukan : ')
kapital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
snake_case = ''

for huruf in camelCase :
    if  (huruf in kapital):
        snake_case = snake_case +'_'+ huruf.lower()
    else :
        snake_case = snake_case + huruf
print(snake_case)
