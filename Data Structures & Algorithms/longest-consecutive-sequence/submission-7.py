class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maximum = 0

        for num in nums:
            length = 1
            
            if num - 1 in seen:
                continue
            
            else:
                while num + 1 in seen:
                    length += 1
                    num = num + 1
            
            maximum = max(length, maximum)
        
        return maximum