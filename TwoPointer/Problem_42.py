class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax = 0
        rightMax = 0
        res = 0
        while r >= l:
            val = min(leftMax, rightMax)
            if (leftMax <= rightMax):
                waterStore = val - height[l]
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                waterStore = val - height[r]
                rightMax = max(rightMax, height[r])
                r -= 1
            if(waterStore > 0):
                res += waterStore
            # print(leftMax, rightMax)
        return res