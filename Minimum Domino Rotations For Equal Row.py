class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        n = len(A)
        def checkCombo(val,A,B):
            swaps = 0
            for i in range(n):
                if A[i] == val: pass

                elif B[i] == val: swaps += 1
                
                else: return n+1
                
            return swaps
        
        min_swaps = n+1
        min_swaps = min(min_swaps,checkCombo(A[0],A,B))
        min_swaps = min(min_swaps,checkCombo(B[0],A,B))
        min_swaps = min(min_swaps,checkCombo(A[0],B,A))
        min_swaps = min(min_swaps,checkCombo(B[0],B,A))
        
        if min_swaps > n: return -1
        return min_swaps
        