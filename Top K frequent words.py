class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        table = {}
        res = []
        
        for word in words:

            if word not in table:
                table[word] = 0
                
            else:
                table[word] += 1
                
        
        table_list = list(zip(table.keys(),table.values()))
        table_list.sort(key= lambda x: x[1], reverse=True)
        
        freq = 0
        
        for i in range(len(table_list)):
            if table_list[i][1] == table_list[freq][1]:
                continue
                
            temp = table_list[freq:i]
            temp.sort()
            table_list[freq:i] = temp
            freq = i
            
        temp = table_list[freq:i+1]
        temp.sort()
        table_list[freq:i+1] = temp
            
        for i in range(k):
            res.append(table_list[i][0])
            
        return res
            