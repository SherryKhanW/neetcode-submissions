class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for i in range(len(strs)):
            count = [0] * 26
            for j in strs[i]:
                count[ord(j) - ord("a")] += 1
            
            hashmap[tuple(count)].append(strs[i])
        
        return list(hashmap.values())
