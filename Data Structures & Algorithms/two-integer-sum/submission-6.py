class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = []

        for i in range(len(nums)):
            if nums[i] in remain:
                return [remain.index(nums[i]), i]
            remain.append(target - nums[i])

        # 5,5 nums[i] = 5, not in remain -> remain[0] = 5, remain = [5]
        # nums[i] = 5 in remain = [5] => retun []