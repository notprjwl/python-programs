# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        while i>0: 
            if (arr[i-1] > temp):
                arr[i], arr[i-1] = arr[i-1], arr[i]
            i-=1
    return arr


arr = [4, 3, 2, 10, 12, 1, 5, 6]
print(insertion_sort(arr))