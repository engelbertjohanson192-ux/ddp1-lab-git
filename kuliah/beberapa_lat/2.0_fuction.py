def my_fuction (str, huruf = 'i'):
    counter = 0
    for i in str :
        if i == huruf:
            counter +=1

    return counter

print(my_fuction('abadii iii'))
print(my_fuction('abadii iii' , 'a'))
print(my_fuction('aku jago','a'))