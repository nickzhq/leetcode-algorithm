class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        sta = []
        res = ""
        for idx,ele in enumerate(S):
            if ele == "(":
                sta.append( (idx, ele) )
            else:
                if ele == ")" and sta[-1][1] == "(":
                    temp = sta.pop()
                    if len(sta) == 0:
                        res += S[ temp[0] + 1: idx ]
        
        return res
            
        