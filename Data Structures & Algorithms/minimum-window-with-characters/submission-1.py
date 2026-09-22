class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, countT = {}, {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        have, need = 0, len(countT)
        minLen = float('infinity')
        bestLeft, bestRight = 0, 0
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1
                while have == need:
                    if right - left + 1 < minLen:
                        minLen = right - left + 1
                        bestLeft, bestRight = left, right

                    removedLetter = s[left]
                    window[removedLetter] -= 1
                    if removedLetter in countT and window[removedLetter] < countT[removedLetter]:
                        have -= 1
                    left += 1

        return s[bestLeft:bestRight + 1] if minLen != float('infinity') else ""
            
        