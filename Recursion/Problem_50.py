"""
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == -1:
            return 1/x
        if n == 1:
            return x
        return self.myPow(x*x, n//2) * self.myPow(x, n % 2)
        
Solution().myPow(0.00001,2147483647)