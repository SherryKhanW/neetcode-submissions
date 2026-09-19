class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in nums[i+1:]:
                return [i, nums.index(remainder, i + 1)]