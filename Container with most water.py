class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        n = len(height)
        
        front = 0
        back = n-1
        
        area = 0
        
        while front != back:
            
            if height[front] > height[back]:    #move back  
                area = max(area,height[back]*(back-front))     
                back -= 1
            else:                               #move front
                area = max(area,height[front]*(back-front))     
                front += 1
                
        return area