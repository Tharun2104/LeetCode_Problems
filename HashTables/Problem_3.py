"""
3. Longest Substring Without Repeating Characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        Set1 = set()
        res = 0
        for p2 in range(len(s)):
            while s[p2] in Set1:
                Set1.discard(s[p1])
                p1+=1
            Set1.add(s[p2])
            res = max(res, p2-p1+1)
        return res