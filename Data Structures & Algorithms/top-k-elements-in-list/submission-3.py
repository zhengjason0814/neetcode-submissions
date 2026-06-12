class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq, frequency = {}, [[] for i in range(len(nums) + 1)]
        answer = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            frequency[value].append(key)
        
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer