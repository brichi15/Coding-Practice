import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals.sort(key=lambda x: x[0])       
        heap = []
        
        for start,end in intervals:
            
            if heap:
                h_end,h_start = heapq.heappop(heap)
                if h_end > start:
                    heapq.heappush(heap,(h_end,h_start))
                
            heapq.heappush(heap,(end,start))
            
        return len(heap)
            