class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        
        i = 0
        
        while i < len(s):
            
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                past_ind = stack.pop()
                sub_string = list(s[past_ind+1:i])
                sub_string.reverse()
                s = s[:past_ind] + "".join(sub_string) + s[i+1:]
                i -= 2
            
            i += 1
                
        return s
            
            