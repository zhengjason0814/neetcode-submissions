class Solution:
    def isValid(self, s: str) -> bool:
        balanced = []

        for char in s:
            if char == "(":
                balanced.append("(")
            elif char == "{":
                balanced.append("{")
            elif char == "[":
                balanced.append("[")
            elif char == ")":
                if len(balanced) == 0 or balanced.pop() != "(":
                    return False
            elif char == "}":
                if len(balanced) == 0 or balanced.pop() != "{":
                    return False
            elif char == "]":
                if len(balanced) == 0 or balanced.pop() != "[":
                    return False
        if len(balanced) > 0:
            return False
        return True