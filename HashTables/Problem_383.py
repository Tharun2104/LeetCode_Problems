"""
383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

"""
from collections import Counter

ransomNote = "a"
magazine = "b"

# Approach 1: Using Dict TC - O(N), SC - O(2N)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = dict(Counter(ransomNote))
        b = dict(Counter(magazine))
        for i in a:
            if( i in b):
                if(a[i] <= b[i]):
                    pass
                else:
                    return False
            else:
                return False
        return True
    
Solution().canConstruct(ransomNote,magazine)

# Approach 2 :  Using sets TC - O(N), SC - O(N)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = set(ransomNote) 
        for i in a:
            if magazine.count(i)<ransomNote.count(i):
              return(False)
              break
        else:
            return(True)
        
Solution().canConstruct(ransomNote,magazine)