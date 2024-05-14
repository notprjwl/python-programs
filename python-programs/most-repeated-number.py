def most_repeated_number(arr):
    arr.sort()
    result = {}
    count = 0
    for i in range(len(arr)):
        if arr[i] not in result:
            result[arr[i]] = count + 1
        else:
            result[arr[i]] += 1 
    
    maximum_val = 0
    max_key = None
    for key, value in result.items():
        if value >= maximum_val:
            maximum_val = value
            max_key = key
    return max_key
            

print(most_repeated_number(arr=[3,2,3,4,2,3,4,3]))