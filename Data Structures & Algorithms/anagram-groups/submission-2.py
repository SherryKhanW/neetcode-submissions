from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for alphabet in word:
                count[ord(alphabet) - ord("a")] += 1

            key = tuple(count)

            seen[key].append(word)

        return list(seen.values())
        
        