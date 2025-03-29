class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> list[str]:
        lenStr, i = 0, 0
        res = []
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            lenStr = int(s[i:j])
            res.append(s[j+1 : j+1+lenStr])
            i = j+1+lenStr
        return res