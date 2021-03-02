class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(s)
        
        stack = []
        wrong = []
        
        for i in range(len(s)):
            if s[i] == "(": 
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    wrong.append(i)
                    
        
        total = sorted(stack + wrong,reverse=True)
        
        for ind in total:
            del s[ind]
        return "".join(s)