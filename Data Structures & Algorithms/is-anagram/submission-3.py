class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringOne, stringTwo = "".join(sorted(s)), "".join(sorted(t))
        return stringOne == stringTwo