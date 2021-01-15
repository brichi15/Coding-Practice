class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        res = 0
        scale = ""
        
        for i in range(len(num1)-1,-1,-1):
            carry = 0
            cur_num = ""
            for j in range(len(num2)-1,-1,-1):
                
                temp = int(num1[i])*int(num2[j]) + carry
                carry = int(temp/10)
                temp = temp%10
                
                cur_num = str(temp) + cur_num
            if carry > 0:
                cur_num = str(carry) + cur_num
            print(cur_num + scale)
            res += int(cur_num + scale)
            scale += "0"

        return str(res)