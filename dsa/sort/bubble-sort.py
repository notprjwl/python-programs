# Write a Python program to sort a list of elements using the bubble sort algorithm.

def bubble_sort(list1):
    for outer in range(len(list1)-1):       #outerloop so it check all the elements over and over again till the length of the array
        for elem in range(len(list1)-1):
            if list1[elem] > list1[elem+1]:   #comparing logic
                list1[elem], list1[elem+1] = list1[elem+1], list1[elem]     #swapping
            else:
                elem += 1  #moving to next index if the element is not greater                          
    return list1            
    



list1 = [5, 2, 8, 1, 9]
print(bubble_sort(list1))