class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        intervals.sort(key= lambda x: x[0])
        
        i = 0
        past_end = -1
        
        while i < len(intervals):
            
            if intervals[i][0] <= past_end:
                
                if intervals[i][1] <= past_end:
                    del intervals[i]
                    continue
                else:
                    intervals[i][0] = intervals[i-1][0]
                    del intervals[i-1]
                    i -= 1
            
            past_end = intervals[i][1]
            i += 1
            
        return intervals
                