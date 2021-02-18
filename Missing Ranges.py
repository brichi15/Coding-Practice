class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        prev = lower-1
        n = len(nums)
        
        res = []
        for i in range(n+1):
            num = nums[i] if i < n else upper+1
            if num-prev > 2:
                res.append("{}->{}".format(prev+1,num-1))
            elif num-prev == 2:
                res.append(str(num-1))
                
            prev = num
                
        return res