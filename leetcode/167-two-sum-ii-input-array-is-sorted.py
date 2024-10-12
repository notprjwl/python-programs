def twoSum(numbers, target):
    # TIME LIMIT EXCEEDED ERROR
    # for i in range(len(numbers)):
    #     for j in range(i+1, len(numbers)):
    #         if numbers[i] + numbers[j] == target:
    #             # print(i, j)
    #             # print([i+1, j+1]) 
                
    #             return [i+1, j+1]
    
    left, right = 0, len(numbers)-1
    
    while left < right:
        currSum = numbers[left] + numbers[right]
        
        if currSum == target:
            return [left + 1, right + 1]
        elif currSum < target:
            left += 1
        else:
            right -= 1
    return []
    
                
            
print(twoSum(numbers = [2,7,11,15], target = 9))