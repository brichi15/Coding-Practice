class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        
        table = {}
        
        n = len(ppid)
        for i in range(n):
            
            if ppid[i] not in table:
                table[ppid[i]] = [pid[i]]
                
            else:
                table[ppid[i]].append(pid[i])
                  
        def killChildren(proccess):
            deadList = []
            if proccess in table: 
                for child in table[proccess]:
                    deadList += killChildren(child)
                
            deadList.append(proccess)
            return deadList
        
        return killChildren(kill)
                