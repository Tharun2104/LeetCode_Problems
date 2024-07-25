"""
https://leetcode.com/problems/climbing-stairs/
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        def test(n,memo):
            if(n== 1):
                return 1
            if(n==2):
                return 2
            if(n not in memo):
                memo[n]= test(n-1,memo)+test(n-2,memo)
            return memo[n] 
        return test(n,{})
        
n = 44
Solution().climbStairs(n)