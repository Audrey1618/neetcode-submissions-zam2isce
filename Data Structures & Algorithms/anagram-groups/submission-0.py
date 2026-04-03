class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = {}
    
        for i in range(len(strs)):
            ordered = "".join(sorted(strs[i]))
            #print(ordered)
            if ordered not in resultDict:
                resultDict[ordered] = []
            resultDict[ordered].append(strs[i])
            # resultDict[ordered] = [resultDict.get(ordered, i)].append(i)
        #print(resultDict.values())
        return list(resultDict.values())
        