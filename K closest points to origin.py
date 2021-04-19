class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        points.sort(key= lambda x: sqrt(x[0]**2 + x[1]**2))
        return points[:K]

## nlog(k) solution

from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist_arr = map(lambda x: [sqrt(x[0]**2 + x[1]**2)] + x, points)
        
        max_heap = []
        
        for point in dist_arr:
            point[0] *= -1
            p_tuple = tuple(point)
            
            if len(max_heap) < k:
                heapq.heappush(max_heap,p_tuple)
                
            else: ## equal k:
                heapq.heappushpop(max_heap,p_tuple)
                
        return list(map(lambda x: x[1:], max_heap))