class TestSolution:
    def test_is_valid_parentheses_true(self):
        assert Solution().is_valid(s="(){}[]") is True

    def test_is_valid_parentheses_false(self):
        assert Solution().is_valid(s="(") is False
