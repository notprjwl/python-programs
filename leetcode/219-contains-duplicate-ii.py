def containsNearbyDuplicate(nums, k):
    # i = 0
    # while i < len(nums) - 1:
    #     if nums[i] == nums[i+1] and abs(i - (i+1)) <= k:
    #         # print(i, i+1)
    #         return True
    #     i+=1

    
    # for i in range (len(nums)):
    #     print(i)
    #     for j in range(i+1, len(nums)):
    #         if nums[i] == nums[j] and abs(i - j) <= k:
    #             return True
    # return False
    
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] not in hash_map:
            hash_map[nums[i]] = i
        else:
            if abs((i - hash_map.get(nums[i])) <= k):
                return True
            hash_map[nums[i]] = i
    print(hash_map)
    return False

    


print(containsNearbyDuplicate(nums = [1,0,1,1], k = 1))