# Write a Python program to remove duplicates from a list.

def remove_duplicates(list1):
    final_list = []
    for i in list1:
        if i not in final_list:
            final_list.append(i)
        else:
            i+=1
    
    return final_list
    
    


list1 = [1,2,3,5,6,9,1,2,5,3,9,10]
print(remove_duplicates(list1))