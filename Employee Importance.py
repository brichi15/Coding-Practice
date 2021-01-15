"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        employee_table = {}
        
        for employee in employees:
            employee_table[employee.id] = employee
            
            
        def findImportance(id,employees):
            
            queue = [id]
            res = 0
            while queue:
                emp_data = employees[queue.pop(0)]
                print(emp_data.id)
                res += emp_data.importance
                for emp in emp_data.subordinates:
                    queue.append(emp)
            return res
        
        return findImportance(id,employee_table)
                
            