def removeDuplicates(nums):
    # result = []
    # for i in nums:
    #     if i not in result:
    #         result.append(i)
    #     else: i+=1
    
    # return result
    i = 0
    for j in range(1, len(nums)):
        if nums[j]!=nums[i]:
            i += 1
            nums[i] = nums[j]
        else:
            j+=1
    return i+1


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))