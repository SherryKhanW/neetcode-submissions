class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        res = []

        for i in nums:
            if i-1 in unique_nums:
                continue
            else:
                start = i
                length = 1

                while start+1 in unique_nums:
                    start += 1
                    length += 1

                res.append(length)
        
        return max(res) if res else 0
