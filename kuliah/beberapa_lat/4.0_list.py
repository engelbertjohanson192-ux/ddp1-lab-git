my_list = [3, 5, 7, 9]
new_list = my_list

# metod .extend membuat = list lainnya ikut beruba tapi kalau metode duluan
# kalau + hanya list itu saja yang berubah dan walauapun di tambah metode tetep ga beruba

my_list.extend([10,11])
my_list=my_list+[5, 7]

print(my_list)
[3, 5, 7, 9, 5, 7]
print(new_list)