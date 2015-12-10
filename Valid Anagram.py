__author__ = 'Nick'

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        if len(s) != len(t):
            return False

        list_s = [0]*26
        list_t = [0]*26
        # ord() : Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
        # 'a' is 97
        for ch in s:
            list_s[ord(ch)-97] += 1
        for ch in t:
            list_t[ord(ch)-97] += 1

        return list_s == list_t
        '''

        #  map() expects an N-argument function for N sequences
        return set(s) == set(t) and map(s.count,sorted(list(set(s)))) == map(t.count,sorted(list(set(s))))

print( ord("A") )
