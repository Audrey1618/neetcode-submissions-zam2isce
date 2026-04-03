class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       half = [" "] * len(nums)

       for i in range(len(nums)):
            if nums[i] in half:
                return [nums.index(target - nums[i]), i]
            half[i] = target - nums[i]
        
