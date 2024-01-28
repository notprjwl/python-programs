# Write a Python program to find the common elements between two lists.

def common_elements(list1, list2):
    final_list = []
    for item in list1:
        if item in list2:
            final_list.append(item)
            
    return final_list


list1 = [1,2,3,5,6,9]
list2 = [1,2,5,3,9,10]

print(common_elements(list1, list2))  