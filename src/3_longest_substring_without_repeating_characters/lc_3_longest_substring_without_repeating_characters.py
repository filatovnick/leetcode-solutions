class Solution:
    def longest_unique_substring(self, s: str) -> int:
        result = ""
        # Result
        max_length = 0

        # Return 0 if s is empty
        # or 1 if length of string is 1
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        for c in s:
            if c in result:
                result = result[result.find(c) - 1]
            result = result + c
        max_length = max(max_length, len(result))

        return max_length


if __name__ == '__main__':
    print(Solution().longest_unique_substring(s="ohvhjdml"))
    print(Solution().longest_unique_substring(s="abcabcbb"))
    print(Solution().longest_unique_substring(s="bbbbb"))
    print(Solution().longest_unique_substring(s="pwwkew"))
