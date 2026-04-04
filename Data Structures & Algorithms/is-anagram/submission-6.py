class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        existS = [0] * 26
        existT = [0] * 26
        for c in s:
            existS[ord(c) - ord('a')] += 1
        for c in t:
            existT[ord(c) - ord('a')] += 1
        if existS == existT:
            return True
        return False
            