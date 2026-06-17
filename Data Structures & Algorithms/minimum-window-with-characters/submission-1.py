from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = 0

        ans = ""
        min_len = float('inf')

        for right in range(len(s)):

            # include s[right] in window
            if s[right] in need:
                need[s[right]] -= 1

            # check if window contains all required chars
            while all(v <= 0 for v in need.values()):

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left:right+1]

                # remove left character
                if s[left] in need:
                    need[s[left]] += 1

                left += 1

        return ans