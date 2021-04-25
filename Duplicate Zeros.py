class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        z_count = 0
        for num in arr:
            if num == 0: z_count += 1
        
        n = len(arr)
        
        ch_point = n-1
        wr_point = n-1
        
        while wr_point >= 0:
            if arr[ch_point] == 0:
                if ch_point+z_count < n:
                    arr[wr_point] = 0
                    wr_point -= 1
                    
                z_count -= 1
                
                if ch_point+z_count < n:
                    arr[wr_point] = 0
                    wr_point -= 1
                    
            elif ch_point+z_count < n:
                arr[wr_point] = arr[ch_point]
                wr_point -= 1
                
            ch_point -= 1