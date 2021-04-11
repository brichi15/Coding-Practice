class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        arr = input.split("\n")
        stack = []
        
        max_len = 0
        
        for entity in arr:
            tab_count = 0
            
            while entity[tab_count] == "\t":
                tab_count += 1
            
            while stack and tab_count < len(stack): stack.pop()
            stack.append(entity[tab_count:])

            print(stack)
            if "." in entity:
                max_len = max(max_len,len("/".join(stack)))
                
        return max_len