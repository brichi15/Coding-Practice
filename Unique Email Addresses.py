class Solution:
    def numUniqueEmails(self, emails):
        domains = {}
        ans = 0
        
        for em in emails:
            loc,dom = em.split("@")
            nloc = ""
            for ch in loc:
                if ch == '+':
                    break
                elif ch != '.':
                    nloc = nloc+ ch  
            loc = nloc + dom
            
            if not(loc in domains):
                domains[loc] = 1
                ans +=1
        
        return ans