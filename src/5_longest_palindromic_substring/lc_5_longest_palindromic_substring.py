import re


class Solution:
    def longest_palindromic_substring(self, s: str) -> str:
        res = ""
        s = re.sub(r'[\W]', '', s).lower()
        for i in range(len(s)):
            current = self.expand_around_middle(s, i - 1, i + 1)
            in_between = self.expand_around_middle(s, i, i + 1)
            res = max(res, current, in_between, key=len)
        return res

    def expand_around_middle(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
