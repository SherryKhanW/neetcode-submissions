class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            remaining_sum = target - num

            if remaining_sum in seen:
                return [seen[remaining_sum], index]
            
            seen[num] = index
