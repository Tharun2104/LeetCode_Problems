class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]

        #  XOR Operation ( return True only for different i/p)
        res = 0
        for num in nums:
            res = res^num

        # only unique element remains ( 4^1^2^1^2 = (1^1) ^ (2^2) ^ (4))
        return res 
        