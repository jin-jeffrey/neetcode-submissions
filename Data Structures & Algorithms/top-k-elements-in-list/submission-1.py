from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []

        for value, count in freq.items():
            heapq.heappush(heap, (count, value))

            if len(heap) > k:
                heapq.heappop(heap)

        return [value for count, value in heap]