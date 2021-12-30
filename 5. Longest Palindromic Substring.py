# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        
        dp = [[False for _ in range(size)] for _ in range(size)]
        
        for i in range(size):
            dp[i][i] = True
            
        max_len = 1
        start_index = 0
        
        for i in range(1, size):
            for j in range(0, i):
                if s[i] == s[j]:
                    if i - j < 3:
                        dp[j][i] = True
                    else:
                        dp[j][i] = dp[j+1][i-1]
                        
                if dp[j][i]:
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        start_index = j
        
        return s[start_index:start_index + max_len]
        