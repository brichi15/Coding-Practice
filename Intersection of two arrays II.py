class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        intersection = []
        
        common = {}
        
        for num in nums1:                   # keep track of how many of each num in nums1
            
            if num not in common.keys():
                common[num] = 1
                
            else:
                common[num] += 1
                
                
        for num in nums2:
            
            if (num in common.keys()) and (common[num] > 0):
                common[num] -= 1
                intersection += [num]
            
        return intersection
                    
        