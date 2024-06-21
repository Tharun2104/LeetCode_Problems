"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

"""
# Approach : Binary search - TC - O(LogN)
x = 4
class Solution:
    def mySqrt(self, x: int) -> int:
        L , R = 1, x
        while (L <= R):
            M = (L+R)//2   # Finding mid value
            target = M*M
            if(target == x):  # Checking if its equal to target
                return M
            elif(target<x): 
                L = M+1  # Moving the left pointer to mid plus one
            else:
                R = M-1 # Moving the right pointer to mid minus one
        return R
Solution().mySqrt(x)