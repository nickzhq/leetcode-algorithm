class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = []
        for word in words:
            temp_str = ""
            for letter in word:
                temp_str += codes[ ord(letter) - 97 ]
            trans.append( temp_str )
            
        # trans = set(trans)
        res = {}
        for ele in trans:
            # hash_ele = hash(ele)
            res[ele] = 0
        
        return len(res.keys())
        