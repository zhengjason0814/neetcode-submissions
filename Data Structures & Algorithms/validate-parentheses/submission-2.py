class Solution:
    def isValid(self, s: str) -> bool:
        balanced = []
        length = len(s)
        if length == 0:
            return True
        if length == 1:
            return False

        for char in s:
            match char:
                case "(":
                    balanced.append("(")
                case "{":
                    balanced.append("{")
                case "[":
                    balanced.append("[")
                case ")":
                    if len(balanced) == 0 or balanced.pop() != "(":
                        return False                    
                case "}":
                    if len(balanced) == 0 or balanced.pop() != "{":
                        return False                                        
                case "]":
                    if len(balanced) == 0 or balanced.pop() != "[":
                        return False
        if len(balanced) > 0:
            return False
        return True