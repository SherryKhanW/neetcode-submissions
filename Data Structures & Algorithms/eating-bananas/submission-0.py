class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1 , max(piles)
        minimum = r

        def time_taken(piles, m):
            h = 0
            for i in piles:
                h += math.ceil(i / m)
            
            return h

        while l <= r:
            m = (l+r) // 2
            if time_taken(piles, m) > h:
                l = m + 1

            elif time_taken(piles, m) <= h:
                minimum = min(minimum, m)
                r = m - 1

        
        return minimum



