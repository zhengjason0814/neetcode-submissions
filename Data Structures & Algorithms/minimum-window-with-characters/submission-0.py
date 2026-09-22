class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Two dictionaries, one keeping count of whats in the current substring, one with the counter of chars in t
        # Use a sliding window approach, end when right edge reaches the end of the array
        # Everytime we move the window left, we add to the window dict and check if we've satisfied a distinct char requirement
        # If we do, increment "have" variable by one.
        # If we satisfied all distinct char requirements, we update the current shortest substring if its smaller
        # Then, we start updating left window, removing occurences in window as we go. If we remove a char in counterT, we check if the condition is still met. Everytime the conditions are still met, try and update shortest substring if its possible.
        # If we no longer meet the condition after moving left, then we go back to updating the right pointer.

        minSS = ""
        minSSlen = float('infinity')
        window, countT = {}, {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        satisfy = False
        have, need = 0, len(countT)
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1
                if have == need:
                    currentSS = s[left:right + 1]
                    if len(currentSS) < minSSlen:
                        minSS = s[left:right + 1]
                        minSSlen = len(currentSS)
                    satisfy = True
            if satisfy:
                while satisfy:
                    currentSS = s[left:right + 1]
                    if len(currentSS) < minSSlen:
                        minSS = s[left:right + 1]
                        minSSlen = len(currentSS)
                    removedLetter = s[left]
                    window[removedLetter] -= 1
                    left += 1
                    if removedLetter in countT and window[removedLetter] < countT[removedLetter]:
                        have -= 1
                        satisfy = False

        return minSS
            
        