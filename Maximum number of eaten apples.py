import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        if not apples: return 0

        p_que = []
        
        n = len(apples)
        i = 0
        apple_count = 0
        while i<n or p_que:
            if i < n:
                heapq.heappush(p_que,(i+days[i],apples[i]))
            
            exp_date,num_apples = heapq.heappop(p_que)
            while p_que and (i >= exp_date or num_apples <= 0): 
                exp_date,num_apples = heapq.heappop(p_que)
                
            if exp_date > i and num_apples > 0:
                num_apples -= 1
                apple_count += 1
                heapq.heappush(p_que,(exp_date,num_apples))
            
            i += 1
        return apple_count
            