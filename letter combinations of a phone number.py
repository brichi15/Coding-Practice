class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        ans = []
        combo = ""

        def dfs(digits,combo):

            if not digits: 
                ans.append(combo)
                return

            digit = int(digits[0])

            for letter in letters[digit]:

                combo += letter
                dfs(digits[1:],combo)
                combo = combo[:-1]

                
        if not digits: return digits

        dfs(digits,combo)
        
        return ans
            
        