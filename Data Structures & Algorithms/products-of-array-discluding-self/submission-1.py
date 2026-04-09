class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums)

        res = []

        for i in range(len(nums)):
            multi = 1
            for j in range(start, i):
                multi = multi * nums[j]
            for k in range(i + 1, end):
                multi = multi * nums[k]
            res.append(multi)
        return res
        
            