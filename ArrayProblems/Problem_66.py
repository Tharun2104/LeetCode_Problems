class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        revDigits = digits[::-1]
        carry = 1
        for i in range(len(revDigits)):
            if(revDigits[i] == 9):
                revDigits[i] = revDigits[i] + carry
                revDigits[i] = 0
                carry = 1
            elif(revDigits[i] != 9):
                revDigits[i] = revDigits[i] + carry
                carry = 0
                break
        
        if ( carry == 1):
            revDigits.append(carry)
        
        return revDigits[::-1]


"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            digits[i] = 0

            if i == 0:
                return [1] + digits
"""