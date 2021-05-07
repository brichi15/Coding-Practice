class Solution:
    def decodeString(self, s: str) -> str:
        
        def generateString(s):
            new_str = ""
            num_count = 0

            ind = 0
            n = len(s)
            while ind < n:

                if s[ind] >= "0" and s[ind] <= "9":
                    num_count += 1

                elif s[ind] == "[":

                    multiplier = int(s[ind-num_count:ind])
                    sub_str,sub_ind = generateString(s[ind+1:])
                    new_str += multiplier*sub_str

                    num_count = 0
                    ind += sub_ind + 1

                elif s[ind] == "]":
                    return (new_str,ind)

                else:
                    new_str += s[ind]
                    
                ind += 1
                
            return (new_str,ind)
                
        return generateString(s)[0]
