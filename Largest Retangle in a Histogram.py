class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        p_stack = []
        h_stack = []
        
        max_area = 0
        
        for i,height in enumerate(heights):
            
            prev_p = i
            while h_stack and height <= h_stack[-1]: 
                prev_h = h_stack.pop()
                prev_p = p_stack.pop()
                max_area = max(max_area,prev_h*(i-prev_p))
                
            h_stack.append(height)
            p_stack.append(prev_p)
            
        while h_stack:
            height = h_stack.pop()
            pos = p_stack.pop()
            
            max_area = max(max_area,height*(n-pos))
            
        return max_area