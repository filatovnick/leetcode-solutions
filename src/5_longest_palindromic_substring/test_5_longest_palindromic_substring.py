import pytest

from lc_5_longest_palindromic_substring import Solution


class TestSolution:
    @pytest.mark.parametrize("input_string, expected_result", [
        ("assa", "assa"),
        ("astsa", "astsa"),
        ("asdjkaaeaaqwlf", "aaeaa"),
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("a", "a"),
        ("aqw qrty", "qwq"),
        ("XabAx", "xabax"),
        ("xabay", "aba")

    ])
    def test_longest_palindromic_substring(self, input_string, expected_result):
        assert (
                Solution().longest_palindromic_substring(s=input_string)
                == expected_result
        )
