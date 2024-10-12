def rotate(nums, k):
    for i in range(k):
        for j in range(len(nums)-1, 0, -1):
            print(nums[j])
            nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums       
        

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))