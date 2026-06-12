class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for item in nums:
            count[item] = count.get(item, 0) + 1
        for number, count in count.items():
            freq[count].append(number)
        
        answer = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                answer.append(num)
            if len(answer) == k:
                return answer
