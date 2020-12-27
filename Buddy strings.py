class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        
        n = len(B)
        
        if len(A) != n: return False
            
        diff = []
        dupe = {}
        
        for i in range(n):
            if A[i] != B[i]:
                diff.append(i)
            else:
                if A[i] not in dupe:
                    dupe[A[i]] = 0
                else:
                    dupe[A[i]] += 1
                
        
        if len(diff) == 0 and any(dupe.values()): return True
        
        if len(diff) == 2 and A[diff[0]] == B[diff[1]] and B[diff[0]] == A[diff[1]]:
            return True
        
        
        
        return False