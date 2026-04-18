class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            # print(length)
            # print(j)
            
            res.append(s[j + 1: length + j + 1])
            i = j + 1 + length
        return res

            # if s[i] not #, we havent' reached #, iterate,