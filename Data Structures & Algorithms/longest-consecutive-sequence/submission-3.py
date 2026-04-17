class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        maxLen = 1
        
        if not nums:
            return 0

        for num in nums:
            prev = 1
            res = 0
            while num - prev in nums:
                prev -= 1
                res += 1
                maxLen = max(maxLen, res)
        return maxLen   
        #2
        #20
        #4 3 
        