class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = defaultdict(list)
    
        for s in strs:
            ordered = "".join(sorted(s))
            resultDict[ordered].append(s)

        return list(resultDict.values())
        