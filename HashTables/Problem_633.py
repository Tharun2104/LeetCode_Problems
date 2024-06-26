"""
633. Sum of Square Numbers
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

"""
from math import sqrt
c = 5
# Approach 1 : : TC - O(sqrt(N)) SC - O(1)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if(c == 0):
            return True
        for i in range(int(sqrt(c)+1)):
            temp = c - i**2
            if(str((sqrt(temp)))[-1] == "0"):
                return True
        return False
Solution().judgeSquareSum(c)

# Approach 2 : TC - O(sqrt(N)) SC - O(N)
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ump = {}

        for i in range(int(math.isqrt(c)) + 1):
            square = i * i
            ump[square] = ump.get(square, 0) + 1
            req = c - square

            if req in ump:
                return True

        return False

Solution().judgeSquareSum(c)