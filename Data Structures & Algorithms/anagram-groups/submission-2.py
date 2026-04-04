class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            group[sorted_s].append(s)    
        
        res = []

        for value in group.values():
            res.append(value)
        return res
