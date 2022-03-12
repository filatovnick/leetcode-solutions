import pytest


class Solution:
    """"
    Complexity Analysis for Valid Palindrome
    Time complexity: O(N)
    Space complexity:  O(1) Left and Right pointers take up constant space
    """

    def is_palindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[\W]', '', s).lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class TestSolution:
    @pytest.mark.parametrize(
        "input_string, expected_result",
        [
            ("A man, a plan, a canal: Panama", True),
            ("Evil olive", True),
            ("Yo, banana boy!", True),
            (" ", True),
            ("lol", True),
            ("How are you doing?", False),
            ("123!123", False),
        ],
    )
    def test_palindrome(self, input_string, expected_result):
        assert Solution().is_palindrome(input_string) is expected_result
