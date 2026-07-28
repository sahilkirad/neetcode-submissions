class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        dp=[]
        for _ in range(len(s)):
            dp.append([False]*len(s))
        
        start=0
        maxlen=1
        for i in range(len(s)):
            dp[i][i]=True
        
        for length in range(2,len(s)+1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i]==s[j]:
                    if length == 2:
                        dp[i][j] = True  
                    else:
                        dp[i][j] = dp[i + 1][j - 1]   
                if dp[i][j] and length > maxlen:
                    start = i
                    maxlen = length  
        return s[start:start + maxlen]  
