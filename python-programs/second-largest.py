#Write a Python program to find the second largest number in a list.

def second_largest(list1):
    list1 = sorted(list1, reverse = True)
    
    return list1[1]

list1 = [5, 3, 8, 4, 6]
print(second_largest(list1))


#without built-in

def without_built_in(list1):
    for outer in range(len(list1)-1):       
        for elem in range(len(list1)-1):
            if list1[elem] > list1[elem+1]:   
                list1[elem], list1[elem+1] = list1[elem+1], list1[elem]     
            else:
                elem += 1                        
    return list1[-2]

list1 = [5, 3, 8, 4, 6]
print(without_built_in(list1))