# selection sort

def selection_sort(arr):
    for i in range(len(arr)):              
        for j in range(i+1, len(arr)):          # always starting from i+1 and i will be fixed throughout the entire loop. when the value of i in the outer loop changes then j jumps to next pos of i.
            if arr[j] > arr[i]:                 # comparing if 30 < 20 ? true swap else j moves to next index
                arr[i], arr[j] = arr[j], arr[i] # swapping
    return arr
            
        
print(selection_sort([20, 30, 10, 5, 8]))