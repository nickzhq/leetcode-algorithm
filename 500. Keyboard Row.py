# 500. Keyboard Row.py
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("ZXCVBNMzxcvbnm")
        return filter( lambda x: set(x).issubset(row1) or set(x).issubset(row2) or set(x).issubset(row3), words )