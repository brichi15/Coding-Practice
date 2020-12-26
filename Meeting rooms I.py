class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        
        if not intervals:
            return True
        
        table = dict()
        
        for meeting in intervals:
            
            if meeting[0] not in table:
                table[meeting[0]] = meeting[1]
                
            else:
                return False
            
        
        start_times = list(table.keys())
        
        start_times.sort()
        
        end_time = table[start_times[0]]
        
        for s in start_times[1:]:
            
            if end_time > s:
                return False
            
            end_time = table[s]
            
        return True