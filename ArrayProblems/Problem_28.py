"""
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start_1 = 0
        start_2 = 0
        first = True
        store = 0
        while start_1<len(haystack):
            if(haystack[start_1]==needle[start_2]):
                slice1 = haystack[start_1:start_1+len(needle)]
                # print(slice1)
                if(slice1 == needle):
                    return start_1
            start_2 = 0
            start_1+=1
        return -1

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         l,r = 0, 0

#         while l < len(haystack):
#             if haystack[l] == needle[r]:
#                 r += 1
#                 if r == len(needle):
#                     return l - r + 1
#             else:
#                 l -= r  # Move back l to the beginning of the current match attempt
#                 r = 0  # Reset r
#             l += 1
        
#         return -1

haystack = "sadbutsad"
needle = "sad"
Solution().strStr(haystack,needle)
