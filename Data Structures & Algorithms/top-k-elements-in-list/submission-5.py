class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums))]
        for key, val in counter.items():
            bucket[val - 1].append(key)
        
        ans = []
        for i in range(len(bucket) - 1, -1, -1):
            while len(bucket[i]) != 0 and k != 0:
                ans.append(bucket[i].pop())
                k -= 1
        
        return ans

