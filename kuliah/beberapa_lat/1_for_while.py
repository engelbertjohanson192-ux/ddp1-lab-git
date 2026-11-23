my_name = 'sisi bidik'
i = 0

# penggunaan while 
while i < len(my_name) :
    print(my_name[i], end='')
    i+=2
print ('\n')

# penggunaan for tapi colomb 
for letter in my_name[::2] :
    print(letter, end='')
print('\n')

# penggunaan for  
for i in range (0,len(my_name),2):
    print(my_name[i], end='')
print('\n')