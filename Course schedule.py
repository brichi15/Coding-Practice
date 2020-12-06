class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        pre_table = dict()
        
        for element in prerequisites:
            if element[0] not in pre_table: pre_table[element[0]] = [element[1]]     
            else: pre_table[element[0]] += [element[1]]
          
        
        def dfs(course,pre_table,visited):
            
            if course not in pre_table: return True         ##does not have prereq
            
            if course in courses_left: courses_left.remove(course)
            
            ans = True
            for pre in pre_table[course]:
                
                if pre in visited: return False
                visited.add(pre)
                ans = ans and dfs(pre,pre_table,visited)
                visited.remove(pre)
            
            return ans
        
        courses_left = set(range(numCourses))
        
        for course in range(numCourses):
            
            if course not in courses_left: continue
            
            visited = set()
            if not dfs(course,pre_table,visited):
                return False
        
        return True