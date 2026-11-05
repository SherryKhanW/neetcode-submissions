from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for num, cnt in counter.items():
            heapq.heappush(heap, (cnt, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]
