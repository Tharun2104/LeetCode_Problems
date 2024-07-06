"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stck=[-1] # initialize with a start index
        for i in range(len(s)):
            if s[i] == '(':
                stck.append(i)
                # print(stck)
            else:
                stck.pop()
                if not stck: # if popped -1, add a new start index
                    stck.append(i)
                    # print(stck)
                else:
                    # print(stck)
                    # print(i-stck[-1])
                    max_length=max(max_length, i-stck[-1])
        return max_length

s = "()(()"
Solution().longestValidParentheses(s)