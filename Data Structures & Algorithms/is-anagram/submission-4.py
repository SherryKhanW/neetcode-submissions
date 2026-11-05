class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for i in s:
            map1[i] += 1
        
        for j in t:
            map2[j] += 1
        

        return map1 == map2