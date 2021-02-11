class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        def generateCombos(target, combo, start):
            
            if target < 0:
                return
            
            if target == 0:
                res.append(combo)
                return
            
            for i in range(start, len(candidates)):
                
                num = candidates[i]
                generateCombos(target-num,combo + [num], i)
        
        generateCombos(target,[],0)
        return res
