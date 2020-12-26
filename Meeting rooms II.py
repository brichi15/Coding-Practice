import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        
        minHeap = []
        
        heapq.heappush(minHeap,(intervals[0][1],intervals[0][0]))
        
        for next_meet in intervals[1:]:
            
            temp = heapq.heappop(minHeap)
            cur_meet = [temp[1],temp[0]] 
            
            if cur_meet[1] <= next_meet[0]:
                cur_meet = next_meet
            else:
                heapq.heappush(minHeap,(next_meet[1],next_meet[0]))
            
            heapq.heappush(minHeap,(cur_meet[1],cur_meet[0]))
            
        return len(minHeap)
                
            