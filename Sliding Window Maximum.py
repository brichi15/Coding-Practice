class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        dequeue = []
        for i in range(k):
            while dequeue and nums[dequeue[-1]] < nums[i]:
                dequeue.pop()
            dequeue.append(i)
        
        res = [nums[dequeue[0]]]
        
        back = 1
        front = k
        
        
        while front<n:
            
            if dequeue[0] < back:
                dequeue.pop(0)
                
            while dequeue and nums[dequeue[-1]] < nums[front]:
                dequeue.pop()
                
            dequeue.append(front)
            res.append(nums[dequeue[0]])
            
            front += 1
            back += 1
        
        return res