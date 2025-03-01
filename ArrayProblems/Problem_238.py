"""
238. Product of Array Except Self
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

"""
nums = [1,2,3,4]
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []
        # storing prefixes
        product = 1
        for i in nums:  
            output.append(product)
            product = product * i
        # mulyiplying psotifixes with prefixes
        product = 1
        for i in range(len(output)-1,-1,-1): # Iterating backwards till first element
            output[i] = output[i]*product
            product = product * nums[i]
        return output

test = Solution()
test.productExceptSelf(nums)



# Method 2 (revison)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preIn = 0
        preList = []
        for i in range(len(nums)):
            if (i ==0):
                preList.append(1)
                preIn = nums[i]
            else:
                preList.append(preIn)
                preIn = preIn * nums[i]

        preIn = 1
        for i in range(len(nums)-1,-1,-1):
            preList[i] = preList[i]*preIn
            preIn = preIn*nums[i]
        
        return preList





# nums = 4 5 8 1

# res = 48 32 20 160

# [1]

# [1]

# [1,2]

# [2,1]

# O(N)

