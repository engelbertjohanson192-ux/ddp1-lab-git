def sum_nested(nested_list):
    if len(nested_list) == 0:
        return 0
    
    if isinstance(nested_list[0], list):
        return sum_nested(nested_list[0]) + sum_nested(nested_list[1:])
    else:
        return nested_list[0] + sum_nested(nested_list[1:])

print(sum_nested([1,2,3]))
print(sum_nested([1,[2,3],[4,[5,6]]]))
print(sum_nested([1,[2,[3]],4]))
print(sum_nested([]))