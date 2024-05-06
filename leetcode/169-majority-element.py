class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        no_of_times = len(nums) // 2
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        for num, count in count_dict.items():
            if count > no_of_times:
                return num

