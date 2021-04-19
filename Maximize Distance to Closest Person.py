class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        n = len(seats)
        right_side = [0]*n
        
        prev = n*2 + 1
        for i in range(n-1,-1,-1):
            if seats[i] == 1: prev = i
            right_side[i] = prev-i
            
        prev_l = -(n*2) -1
        
        min_dist = 0
        for i in range(n):
            if seats[i] == 1:
                prev_l = i
            else:
                left_d = i-prev_l
                right_d = right_side[i]
                
                if left_d > min_dist and right_d > min_dist:
                    min_dist = min(left_d,right_d)
                    
        return min_dist
            
            