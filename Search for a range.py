class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1,-1]
        
        n = len(nums)
        
        front = 0
        back = n-1
        while front < back:
            mid = int((back+front)/2)
            if nums[mid] >= target:
                back = mid
            else:
                if front == mid: break
                front = mid
            
        front2 = 0
        back2 = n-1
        while front2 < back2:
            mid = int((front2+back2)/2)
            if (front2-back2)%2 == 1: mid += 1
            if nums[mid] <= target:
                front2 = mid
            else:
                if back2 == mid: break
                back2 = mid
            
        if nums[back] == target and nums[front2] == target:
            return[back,front2]
        
        return [-1,-1]