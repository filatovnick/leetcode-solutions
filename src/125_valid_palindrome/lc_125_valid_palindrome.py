import pytest


class Solution:
    def is_palindrome(self, s: str) -> bool:
        p = "".join(ch for ch in s if ch.isalnum()).lower()
        return True if p == p[::-1] else False


class TestSolution:
    @pytest.mark.parametrize(
        "input_string, expected_result",
        [
            ("A man, a plan, a canal: Panama", True),
            ("Evil olive", True),
            ("Yo, banana boy!", True),
            (" ", True),
            ("1", True),
            ("How are you doing?", False),
            ("123!123", False),
        ],
    )
    def test_palindrome(self, input_string, expected_result):
        assert Solution().is_palindrome(input_string) is expected_result
