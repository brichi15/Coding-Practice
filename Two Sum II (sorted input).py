class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        front = 0
        back = len(numbers)-1
        
        while front < back:
            
            cur_sum = numbers[front] + numbers[back]
            
            if cur_sum > target:
                back -= 1
                
            elif cur_sum < target:
                front += 1
                
            else: 
                return [front+1,back+1]