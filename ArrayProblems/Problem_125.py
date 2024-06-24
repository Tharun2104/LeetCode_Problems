"""
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1: Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""
# Two Pointer Approach
s =  "A man, a plan, a canal: Panama"
class Solution:
    def isPalindrome(self,s: str) -> bool:
        start = 0 # Start Pointer
        s = s.lower() # End Pointer
        end = len(s)-1
        # print(end)
        while(end>start):
            if( s[start].isalnum() and s[end].isalnum() ): # considering only alphanum values
                if(s[start] == s[end]):
                    start += 1
                    end -=1
                else:
                    # print(s[start], s[end])
                    return False
            elif( not s[start].isalnum()): # Ignoring which are not alphanum 
                start += 1
            else:   # Ignoring which are not alphanum 
                end -=1
        return True

Solution().isPalindrome(s)