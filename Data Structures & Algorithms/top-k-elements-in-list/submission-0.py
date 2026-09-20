from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        common = count.most_common(k)

        return [i[0] for i in common]

        


        

        

        