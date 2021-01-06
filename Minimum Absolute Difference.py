class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        if len(arr) < 2:
            return []
        
        arr.sort()
        min_abs = (10**6)*2
        
        res = []
        
        for i in range(len(arr)-1):
            
            diff = arr[i+1]-arr[i]
            if diff < min_abs:
                min_abs = diff
                res = [[arr[i],arr[i+1]]]
                
            elif diff == min_abs:
                res.append([arr[i],arr[i+1]]) 
                
        return res