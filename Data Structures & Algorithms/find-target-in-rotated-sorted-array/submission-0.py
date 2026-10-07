class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0 , n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_index = l

        if min_index == 0:
            l, r = 0, n - 1
        elif nums[0] <= target <= nums[min_index - 1]:
            l, r = 0, min_index - 1
        else:
            l, r = min_index, n - 1
        
        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
            
        return -1
