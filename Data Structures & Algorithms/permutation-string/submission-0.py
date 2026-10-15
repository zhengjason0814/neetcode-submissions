class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for char in s1:
            count1[char] = count1.get(char, 0) + 1

        need = len(count1)

        for i in range(len(s2)):
            count2 = {}
            counter = 0
            for j in range(i, len(s2)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1
                if s2[j] not in count1 or count2[s2[j]] > count1[s2[j]]:
                    break
                elif count2[s2[j]] == count1[s2[j]]:
                    counter += 1
                
                if counter == need:
                    return True
        
        return False