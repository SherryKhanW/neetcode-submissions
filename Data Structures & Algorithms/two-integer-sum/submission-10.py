class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,n in enumerate(nums):
            remaining = target - n

            if remaining in seen:
                return [seen[remaining], i]
            
            seen[n] = i
            
        
        