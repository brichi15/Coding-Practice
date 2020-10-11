class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []
        h_map = {}
        scale = ord('a')             ## base letter ascii
        
        for word in strs:      
            key = [0]*26                            ## 26  letters in alphabet
            for letter in word:
                key[ord(letter)-scale] += 1
                
            if tuple(key) not in h_map: h_map[tuple(key)] = [word]
            else: h_map[tuple(key)].append(word)
            
            
        for word_set in h_map.values():
            ans.append(word_set)
            
        return ans