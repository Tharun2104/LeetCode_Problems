class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            l = 0
            eSum = set()
            oSum = set()
            for j in range(i,len(nums)):
                if nums[j] % 2 == 0: eSum.add(nums[j])
                else: oSum.add(nums[j])
                # print(i, eSum, oSum)
                if len(eSum) == len(oSum):
                    l = max(l, j + 1 - i)
            count[i] = l
        # print(count)
        return max(count.values())

"""
2,3,2
1,2,3

o = (3)
e = (2)
l = 2

count[0] = 2


"""