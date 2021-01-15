class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        m = len(version1)
        n = len(version2)
        
        loop_len = max(m,n)
        
        i = 0
        while i < loop_len:
            
            cur_1 = version1[i] if i < m else 0
            cur_2 = version2[i] if i < n else 0
            
            if int(cur_1) > int(cur_2):
                return 1
            if int(cur_2) > int(cur_1):
                return -1
            i += 1
        return 0