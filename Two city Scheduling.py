class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = int(len(costs)/2)                   
        costs.sort(key= lambda x: x[0]-x[1])        # sort by costA - costB
        
        res = 0
        
        for i in range(len(costs)):
            cost = costs[i][0] if i < n else costs[i][1]        # first n people go to city A
            
            res += cost
            
        return res