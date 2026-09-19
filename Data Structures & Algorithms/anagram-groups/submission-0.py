from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # start with first element first compare lengths if equal look at dictionaries if equal they are anagram and if an anagram is found you can also remove that from the search as that has already been classified
 
        cmp_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)  # dictionary keys must be hashable hence must be immutable

            cmp_dict[key].append(word)
        

        return list(cmp_dict.values())
        