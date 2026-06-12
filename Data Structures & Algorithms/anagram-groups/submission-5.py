class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        
        for string in strs:
            sortedWord = "".join(sorted(string))
            answer[sortedWord].append(string)
        return list(answer.values())