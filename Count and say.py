class Solution:
    def countAndSay(self, n: int) -> str:
        
        table = {}
        
        def helper(n):
            if n == 1:
                return str(n)
            
            if n not in table:
                string = helper(n-1)
                table[n] = string
            else:
                string = table[n]

            newString = ""
            counter = 1
            cur_num = string[0]

            for character in string[1:]:
                if cur_num != character:

                    newString += str(counter)+cur_num
                    counter = 1
                    cur_num = character

                else:
                    counter += 1

            newString += str(counter)+cur_num

            return newString
        
        return helper(n)