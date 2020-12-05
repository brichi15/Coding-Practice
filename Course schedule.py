class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_table = dict()
        
        for element in prerequisites:
            if element[0] not in pre_table: pre_table[element[0]] = [element[1]]     
            else: pre_table[element[0]] += [element[1]]
            
        courses_left = set(range(numCourses))
        
        for i in range(numCourses):
            if i not in pre_table:
                courses_left.remove(i)
        
        rem_flag = 1
        
        while rem_flag:
            
            rem_flag = 0
            for pre in pre_table.keys():
                flag = 1
                for course in pre_table[pre]:
                    if course in courses_left: flag = 0

                if pre in courses_left and flag == 1:
                    courses_left.remove(pre)
                    rem_flag = 1
        
        if courses_left: return False
        else: return True
                    