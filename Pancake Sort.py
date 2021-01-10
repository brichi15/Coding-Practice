class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        
        back = n
        
        res = []
        while back > 1:
            
            k = arr.index(back)         ##find largest unsorted element
            
            if back != k+1:
                res.append(k+1)
                temp = arr[:k+1]            ##reverse
                temp.reverse()
                arr[:k+1] = temp

                res.append(back)
                temp = arr[:back]
                temp.reverse()
                arr[:back] = temp
            
            back -= 1
            
        return res