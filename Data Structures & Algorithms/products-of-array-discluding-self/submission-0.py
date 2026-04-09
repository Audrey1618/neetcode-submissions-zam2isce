class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        zero = set()
        multi = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zero.add(i)
            else:
                multi = multi * nums[i]
        
        if len(zero) > 1:
            return res

        for i in range(len(nums)):
            if len(zero) == 1:
                if i in zero:
                    res[i] = multi
                    return res
            else:
                res[i] = int(multi / nums[i])
        return res
            
                
            

        