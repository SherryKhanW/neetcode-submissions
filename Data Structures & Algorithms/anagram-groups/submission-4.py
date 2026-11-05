class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            words_lst = [0] * 26
            for alphabet in word:
                words_lst[ord(alphabet) - ord('a')] += 1

            anagrams[tuple(words_lst)].append(word)
        
        return [vals for vals in anagrams.values()]
            