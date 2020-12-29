import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        hash_table = {}
        
        for num in nums:

            if num not in hash_table:
                hash_table[num] = 0
            else: hash_table[num] -= 1
                
            
        heap = []
            
        for key,val in zip(hash_table.keys(),hash_table.values()):
            heapq.heappush(heap,(val,key))
            
        ans = []
        for i in range(k):
            temp = heapq.heappop(heap)
            ans.append(temp[1])
            
        return ans
        
                