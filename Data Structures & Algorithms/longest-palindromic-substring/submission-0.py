class Solution:
    def expand(self,s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1
    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxLen = 1  
        for i in range(len(s)):
            l, r = self.expand(s, i, i)

            if r - l + 1 > maxLen:
                start = l
                maxLen = r - l + 1

            l, r = self.expand(s, i, i + 1)

            if r - l + 1 > maxLen:
                start = l
                maxLen = r - l + 1
        return s[start:start + maxLen]
       