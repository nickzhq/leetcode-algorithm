# 557. Reverse Words in a String III.py
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # shorter...
        return ' '.join( x[::-1] for x in s.split() )
        # return " ".join(map(lambda x: x[::-1], s.split()))
    '''    result = ""
        for x in s.split():
            result += self.reverse_str(x) + " "
        return result[0: len(result) - 1]
        
    def reverse_str( self, string ):
        return string[::-1]
    '''