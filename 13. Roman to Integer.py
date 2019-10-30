class Solution:
    def romanToInt(self, s: str) -> int:
        
        hold = 'Zero'
        num = 0
        data = {'Zero':0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        for let in s:
            
            
            
            if hold == 'C' and (let == 'D' or let == 'M'): 
                num += (data[let] - data[hold])
                hold = 'Zero'

            elif hold == 'X' and (let == 'C' or let == 'L'):
                num += (data[let] - data[hold])
                hold = 'Zero'

            elif hold == 'I' and (let == 'X' or let == 'V'):
                num += (data[let] - data[hold])
                hold = 'Zero'

            elif let == 'I' or let == 'X' or let == 'C': #possible subtract
                num += data[hold]
                hold = let
          
            else:
                num += (data[let] + data[hold])
                hold = 'Zero'
                
        num += data[hold]
                    
        return num          
                    