class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            bucket[cnt].append(num)

        res = []

        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res