class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            # print(t)
            if s[i] in t:
                t = t.replace(t[t.index(s[i])],"", 1)
            else:
                return False
        return True    



        # if sorted(list(s)) == sorted(list(t)):
        #     return True
        # return False

        # # dict
        # sDict = {}
        # tDict = {}

       

        # for i in range(len(s)):
        #     if s[i] not in sDict:
        #         sDict[s[i]] = 0
        #     if t[i] not in tDict:
        #         tDict[t[i]] = 0
        #     sDict[s[i]] += 1
        #     tDict[t[i]] += 1
        
        # if sDict == tDict:
        #     return True
        # return False