__author__ = 'Nick'

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        count = 0
        for i in range(0,32):
            if ( (n >> i) & 1 == 1 ):
                count += 1
        return count
        '''
        '''
        # more fast
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c
        '''
        c = 0
        while (n/2 != 1):
            if n%2 == 1:
                c+=1
            n /= 2
        return c