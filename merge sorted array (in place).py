class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        n1_ind = m-1
        if m <= 0: n1_ind = m+1
        
        n2_ind = n-1
        
        z_ind = len(nums1)-1
        
        while n2_ind >= 0 and n1_ind >= 0:
     
    
            if n1_ind > m or nums2[n2_ind] >= nums1[n1_ind]:
                nums1[z_ind] = nums2[n2_ind]
                n2_ind -= 1
                z_ind -= 1
                
            else:
                temp = nums1[z_ind]
                nums1[z_ind] = nums1[n1_ind]
                nums1[n1_ind] = temp
                n1_ind -= 1
                z_ind -= 1
            
        if n2_ind >= 0:
            nums1[:z_ind+1] = nums2[:n2_ind+1]
        
        