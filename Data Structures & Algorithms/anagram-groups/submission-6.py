class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}

        for string in strs:
            sortedWord = "".join(sorted(string))
            if sortedWord not in answer:
                answer[sortedWord] = []
            answer[sortedWord].append(string)
        return list(answer.values())