class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string
        return encodedString


    def decode(self, s: str) -> List[str]:
        stringList, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            intLen = int(s[i:j])
            stringList.append(s[j + 1 : j + 1 + intLen])
            i = j + 1 + intLen
        return stringList
 



