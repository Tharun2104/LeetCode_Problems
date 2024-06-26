"""
242. Valid Anagram
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

"""
from collections import Counter
s = "anagram"
t = "nagaram"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(dict(Counter(s)) == dict(Counter(t))):
            return True
        return False
Solution().isAnagram(s,t)