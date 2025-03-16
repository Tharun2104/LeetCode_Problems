class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(not s):
            return True
        pointS = 0
        for i in t:
            if(i == s[pointS]):
                pointS +=1
                if(pointS == len(s)):
                    break
        
        return pointS == len(s)
