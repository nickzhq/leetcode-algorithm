# 187. Repeated DNA Sequences
# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        seen, res = set(), set()
        
        for start in range( n - L + 1 ):
            tmp = s[start:start + L]
            
            if tmp in seen:
                res.add(tmp[:])
                
            seen.add( tmp[:] )
            
        return res
        