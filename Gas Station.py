class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        start_ptr = 0
        while start_ptr < n:
            
            started = False
            trip_ptr = start_ptr
            cur_gas = 0
            while cur_gas >= 0:
                if started and trip_ptr == start_ptr:
                    return start_ptr
                
                started = True
                cur_gas += gas[trip_ptr] - cost[trip_ptr]
                
                trip_ptr = (trip_ptr+1)%n
                
            if trip_ptr <= start_ptr: return -1
            start_ptr = trip_ptr
            
        return -1
                