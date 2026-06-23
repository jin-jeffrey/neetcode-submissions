import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get frequency
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        heap = []
        for value, count in freq.items():
            heapq.heappush(heap, (-1*count, value))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res