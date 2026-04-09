class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        # print(count)

        sortedDict = dict(sorted(count.items(), key=lambda item: item[1], reverse = True))
        
        # print(sortedDict)
        res = []

        #{5: 2, 4: 5, 4: 3, 1: 1}, k = 3 => [2, 5, 3]
        i = 0
        for key in sortedDict.keys():
            if i < k:
                res.append(key)
                i = i + 1
        return res
        

        





