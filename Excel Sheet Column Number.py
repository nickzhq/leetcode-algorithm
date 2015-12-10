__author__ = 'Nick'

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range( 0, len(s)):
            sum += ( ord(s[len(s) - 1 - i ]) - 65 + 1) * 26 ** i
        return sum
    '''
        num = 0
        j = 0
        for i in range(len(s)-1,-1,-1):
            num+= 26**j *(ord(s[i])-64)
            j+=1
        return num
    '''


m = Solution()
print( m.titleToNumber("AAA"))