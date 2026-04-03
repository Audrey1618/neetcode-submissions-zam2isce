class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hash map, to store the number of appearance of a number
        exist = {};

        for i in range(len(nums)):
            if nums[i] not in exist:
                exist[nums[i]] = 1;
            else:
                return True
        return False
        

