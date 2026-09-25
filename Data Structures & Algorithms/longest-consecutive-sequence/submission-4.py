class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        seen = set(nums)

        for i in nums:
            length = 1

            if i - 1 in seen:
                continue
            else:
                while i + 1 in seen:
                    length += 1
                    i = i + 1
            
            max_seq = max(max_seq, length)

        return max_seq
