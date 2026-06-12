class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        stringOne, stringTwo = {}, {}
        for i in range(len(s)):
            stringOne[s[i]] = stringOne.get(s[i], 0) + 1
            stringTwo[t[i]] = stringTwo.get(t[i], 0) + 1
        return stringOne == stringTwo
        