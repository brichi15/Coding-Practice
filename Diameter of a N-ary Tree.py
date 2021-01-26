class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        def dfs(root):
            
            if not root:
                return [-1,0]
            
            first = 0           
            second = 0
            
            m_diam = 0
            for child in root.children:
                length,diam = dfs(child)
                m_diam = max(m_diam,diam)
                if length > first:
                    second = first
                    first = length
                elif length > second:
                    second = length
                
            m_diam = max(m_diam,first+second)
            
            return [first+1,m_diam]
        
        return dfs(root)[1]