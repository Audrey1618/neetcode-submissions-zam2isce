class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        half = {}

        for i in range(len(nums)):
            for val in half.values():
                if nums[i] == val[1]:
                    return [val[0], i]
            half[nums[i]] = [i, target - nums[i]]
        
