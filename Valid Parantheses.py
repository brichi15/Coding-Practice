class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        b_open = {
            "(":0,
            "{":1,
            "[":2
        }
        
        b_close = {
            ")":0,
            "}":1,
            "]":2
        }
        
        for brac in s:
            
            if brac in b_open:
                stack.append(b_open[brac])
                
            else:
                if not stack or stack[-1] != b_close[brac]:
                    return False
                
                stack.pop()
            
            
                
                
        return not stack
            