class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, j in enumerate(nums):
            remaining_sum = target - j

            if remaining_sum in seen:
                return [seen[remaining_sum], i]
            
            seen[j] = i