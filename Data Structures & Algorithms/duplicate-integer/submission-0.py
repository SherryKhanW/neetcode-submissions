class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1;
            else:
                hashmap[num] += 1;

        if any(value > 1 for value in hashmap.values()):
            return True
        else:
            return False
