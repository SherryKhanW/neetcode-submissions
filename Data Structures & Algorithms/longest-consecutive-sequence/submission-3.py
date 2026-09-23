class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)

        res = []

        for num in nums:
            start = num
            length = 1
            if start - 1 in hash_set:
                continue

            else:
                while start + 1 in hash_set:
                    start += 1
                    length += 1

                res.append(length)

        return max(res) if res else 0
                
