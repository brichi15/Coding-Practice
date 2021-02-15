class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        left = []
        max_l = 0
        
        for i in range(n):
            if height[i] > max_l:
                max_l = height[i]
            left.append(max_l)
        
        max_r = 0
        right = []
        
        for i in range(n-1,-1,-1):
            if height[i] > max_r:
                max_r = height[i]
            right = [max_r] + right 
            

        res = 0

        for i in range(n):
            min_peak = min(left[i],right[i])

            if min_peak > height[i]:
                res += min_peak-height[i]
        
        return res

##-------------------------stack method---------------------------------##
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        stack = []
        count = 0
        
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                fill_ind = stack.pop()
                
                if stack:
                    count += (min(height[i],height[stack[-1]])-height[fill_ind]) * (i-stack[-1]-1)
                    
            stack.append(i)
            
        return count