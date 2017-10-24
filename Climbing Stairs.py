__author__ = 'Nick'

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        else:
            first, second = 1, 2
            for i in range(3,n+1):
                temp = first+second
                first = second
                second = temp
            return first+second
        '''
        n += 1
        phi = (1 + pow(5, 0.5)) / 2
        return round( pow(phi,n) / pow(5,0.5) )
        '''