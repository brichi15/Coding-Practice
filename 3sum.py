class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        length = len(nums)
        
        ans = []
        
 
        for i in range(length-2):
        
            if nums[i] == nums[i-1] and i > 0: continue
        
            j = i+1
            k = length-1
            
            while k>j:
                
                if j > i+1 and nums[j] == nums[j-1]:
                    j+=1 
                    continue
                    
                elif k < length-1 and nums[k] == nums[k+1]:
                    k -=1
                    continue

                s = nums[i]+nums[j]+nums[k]

                if s == 0: 
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1

                elif s > 0:
                    k -= 1

                else:
                    j += 1

        return ans
            