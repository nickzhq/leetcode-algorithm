class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # A: 65; a: 97
        res = ""
        for ele in str:
            if ele < 'A' or ele > 'Z' :
                res += ele
            else:
                res += chr(ord(ele) - 65 + 97)
        
        return res