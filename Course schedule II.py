class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre_table = {}
        
        for pre in prerequisites:
            if pre[0] not in pre_table:
                pre_table[pre[0]] = [pre[1]]
            else:
                pre_table[pre[0]].append(pre[1])
               

        visited = set()
        stack = []
        no_pre = []
        
        def dfs(course):
            
            ans = True
            
            if course in stack: return ans
            
            if course not in pre_table: return ans
            
            for pre in pre_table[course]:
                if pre not in visited:
                    visited.add(pre)
                    ans = ans and dfs(pre)
                    visited.remove(pre)
                else:
                    return False
            
            stack.append(course)
            
            return True and ans
        
        
        for course in range(numCourses):
            
            if course not in pre_table:
                no_pre.append(course)
            
            elif course not in stack:
                check = dfs(course)
                if not check: return []
                

        stack = no_pre + stack 
        
        return stack