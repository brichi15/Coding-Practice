class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
    
        carry = 1

        i = len(digits) -1   #start from the end

        while carry:

            if i < 0:
                digits = [1] + digits               # out of range, add a 1 to the end
                break
            
            digits[i] = (digits[i] + 1)%10
            if digits[i] != 0: carry = 0

            i -= 1
        
          
        return digits