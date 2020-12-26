class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        
        if not intervals:
            return True

        intervals.sort(key=lambda x: x[0])
        
        print(intervals)
        
        prev_end = intervals[0][1]
        for meeting in intervals[1:]:
            
            if prev_end > meeting[0]:
                return False
            
            prev_end = meeting[1]
            
        return True
        