class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Hashmap approach
        hashmap = {nums[i]:i for i in range(len(nums))}
        seen = []

        for i in range(len(nums)):
            remaining_sum = target - nums[i]
            seen.append(i)

            if remaining_sum in hashmap and hashmap[remaining_sum] not in  seen:
                return [i, hashmap[remaining_sum]]

                