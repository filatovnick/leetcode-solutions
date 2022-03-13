class Solution:
    def is_valid(self, s: str) -> bool:
        """"
        Usually, the validation of brackets is checked by using a stack.
        Every time we see an open bracket, we push it into the stack.
        Every time we see closed bracket, we check whether the last element in the stack
        is an open bracket. If not, we return false.
        Since we have three types of brackets, we need a hashmap that maps
        open brackets to their close kin.
        """
        if len(s) & 1:
            return False
        stack, hash_map = [], {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in hash_map:
                stack.append(char)
            else:
                if not stack or hash_map[stack[-1]] != char:
                    return False
                stack.pop()
        return not stack
