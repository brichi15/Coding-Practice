class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        count = 0
        o_table = {}
        for letter in order:
            o_table[letter] = count
            count += 1
            
        def isWordBGreater(wordA,wordB):
            
            length = min(len(wordA),len(wordB))
            
            i = 0
            while i < length:
                
                valA = o_table[wordA[i]]
                valB = o_table[wordB[i]]
                
                if valA < valB: return True
                if valA > valB:  return False
                
                i += 1
                
            return len(wordA) <= len(wordB)
        
        for i in range(len(words)-1):
            if not isWordBGreater(words[i],words[i+1]):
                return False
            
        return True