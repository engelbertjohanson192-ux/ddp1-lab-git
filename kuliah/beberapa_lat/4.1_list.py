
str_list = ['Todoroki','Midoriya','Uraraka']
num_list = [3, 47, 15]
num_list[-1] = 25
print(str_list + num_list) # Line 1
print([str_list[0],num_list[-1]]) # Line 2
print(str_list.append(num_list)) # Line 3
print(str_list) # Line 4
print(str_list.extend([127,256])) # Line 5
print(str_list) # Line 6
print(str_list.pop()) # Line 7
print(str_list) # Line 8

# print pas di append ataupun extend none



my = ['AKU suka makan Aku']
result = [word.lower() for word in my[0].split() ]
print (result.count('aku'))