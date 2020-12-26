class Solution:
    def findCelebrity(self, n: int) -> int:
        
        possible = 0
        not_p= set()
        
        for i in range(1,n):    
            if knows(possible,i):
                possible = i
                
        for i in range(n):
            
            if i == possible: continue
                
            if knows(possible,i) or not knows(i,possible): return -1
            
        return possible
                
                
                
        
        