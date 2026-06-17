from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str):

        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        left = 0

        ans_left = 0
        ans_right = 0
        min_len = float("inf")

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans_left = left
                    ans_right = right

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[ans_left:ans_right + 1]