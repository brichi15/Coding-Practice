class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        front = 0
        back = len(nums)-1
        
        if nums[front] == target:
            return front
        
        if nums[back] == target:
            return back
        
        while front < back-1:
            
            mid = int((front+back)/2)
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[front]:
                if nums[front] < target and target < nums[mid]:
                    back = mid
                else:
                    front = mid
            else:
                if nums[mid] < target and target < nums[back]:
                    front = mid
                else:
                    back = mid
                    
        return -1
                    