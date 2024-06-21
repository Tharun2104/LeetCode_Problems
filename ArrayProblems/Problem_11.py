"""
11. Container With Most Water
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, 
the max area of water (blue section) the container can contain is 49.

"""
# Two pointer approach
height = [1,8,6,2,5,4,8,3,7]
class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height)-1
        max = float('-inf')
        while(end>start):
            breath = min(height[start],height[end])
            length = end - start
            area = length*breath
            if ( area> max ):
                max = area
            if(height[start]>height[end]):
                end = end -1
            else:
                start = start + 1
        return max
test = Solution()
print(test.maxArea(height))