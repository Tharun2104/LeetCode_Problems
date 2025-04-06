class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        p1, p2 = 0, 0
        maxf = 0
        while p2 < len(s):
            count[s[p2]] = 1 + count.get(s[p2], 0)
            maxf = max(maxf, count[s[p2]])
            while ((p2 - p1 + 1) - maxf > k ):
                count[s[p1]] -= 1
                p1+=1

            res = max(res, p2 - p1 + 1)
            p2+=1

        return res




# Notes: sliding window technique
# 1. find max number of replacing characters by substracting length of the window with max frequency character which will be stored in the count hash map
# 2. compare the number of replacing characters by k, if number of repeating characters is more increment the left p1 else increment the right p2
# 3. when incrementing the left p1 decrease the frequency in the count
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        p1, p2 = 0, 0
        while p2 < len(s):
            count[s[p2]] = 1 + count.get(s[p2], 0)  # creating the count hash map
            length = p2 - p1 + 1            # window length
            maxf = max(count.values())      # finding the max frq element
            while (length - maxf > k ):     # if number of replacing characters is more
                count[s[p1]] -= 1           # increment the left pointer and decrement the count of that -
                p1+=1                       # - paticular element
                maxf = max(count.values())
                length = p2 - p1 + 1

            if( length - maxf <= k ):
                res = max(res, length)
                p2+=1

        return res
"""



