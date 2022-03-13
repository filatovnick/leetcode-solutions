import pytest

from lc_20_valid_parentheses import Solution


class TestSolution:
    @pytest.mark.parametrize("valid_parentheses", [
        "()[]{}",
        "((([])))",
        "((([]{})))",
        "((([]{}[])))",
        "[((([{()}])))]",
    ])
    def test_is_valid_parentheses_true(self, valid_parentheses):
        assert Solution().is_valid(s=valid_parentheses) is True

    @pytest.mark.parametrize("invalid_parentheses", [
        "{",
        "{}{",
        "[({",
        ")[(",
        "[)][]",
        "((([{]})))",
    ])
    def test_is_valid_parentheses_false(self, invalid_parentheses):
        assert Solution().is_valid(s=invalid_parentheses) is False
