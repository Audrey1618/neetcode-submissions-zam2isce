class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        exist = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            exist[ord(s[i]) - ord('a')] += 1
            exist[ord(t[i]) - ord('a')] -= 1
        print(exist)
        for val in exist:
            if val != 0:
                return False
        return True
            