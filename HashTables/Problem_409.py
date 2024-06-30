"""
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example :
Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_var = dict(Counter(s))
        # print(hash_var)
        l = len(s)
        count = 0
        for i in hash_var:
            if(hash_var[i]%2 == 0):
                pass
            else:
                count = count + 1
        if(count == 0):
            return l-count
        else:
            return l-count+1

s = "abccccdd"
Solution().longestPalindrome(s)