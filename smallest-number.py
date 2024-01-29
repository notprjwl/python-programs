def smallest_number(list1):
    min_num = list1[0]
    for num in list1:
        if min_num > num:
            min_num = num
    
    return min_num
    
    
list1 = [2, 3, 1, 4, 5]
print(smallest_number(list1))