from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        left = 0
        res = 1
        max_freq = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            max_freq = max(counter[s[right]], max_freq)
            substringLen = right - left + 1
            if substringLen - max_freq <= k:
                res = max(res, substringLen)
            else:
                counter[s[left]] -= 1
                left += 1
            
        return res