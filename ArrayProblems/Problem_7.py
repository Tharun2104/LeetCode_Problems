class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1  # Define 32-bit integer range
        res = 0
        sign = -1 if x < 0 else 1  # Store sign
        x = abs(x)  # Work with positive value
        
        while x:
            rem = x % 10
            res = res * 10 + rem
            x //= 10  # Floor division
            
            # Check for 32-bit overflow
            if res > MAX:
                return 0
        
        return sign * res  # Restore original sign