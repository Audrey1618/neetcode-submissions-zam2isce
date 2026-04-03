class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #newNums = nums.sort();
        remain = [0] * len(nums)

        for i in range(len(nums)):
            remain[i] = target - nums[i]
            print(remain[i])
            if remain[i] in nums[i + 1:]:
                return [i, nums.index(remain[i], i + 1)]



