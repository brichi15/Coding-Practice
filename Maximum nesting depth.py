class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = 0
        m_size = 0
        
        for ch in s:
            
            if ch == "(":
                stack += 1
                
            elif ch == ")":
                stack -= 1
                
            if stack > m_size:
                m_size = stack
                
        return m_size