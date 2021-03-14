class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        if n <= 1:
            return nums
        
        left = self.sortArray(nums[:int(n/2)])
        right = self.sortArray(nums[int(n/2):])
        
        res = []
        
        l_ptr = r_ptr = 0

        while l_ptr < len(left) or r_ptr < len(right):
            lval = left[l_ptr] if l_ptr < len(left) else 50001
            rval = right[r_ptr] if r_ptr < len(right) else 50001
            
            if lval <= rval:
                res.append(lval)
                l_ptr += 1
            else:
                res.append(rval)
                r_ptr += 1
            
        return res
        