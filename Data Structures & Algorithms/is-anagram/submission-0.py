class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h_s = {}
        h_t = {}

        for char in s:
            if char not in h_s:
                h_s[char] = 1
            else:
                h_s[char] += 1

        for char in t:
            if char not in h_t:
                h_t[char] = 1
            else:
                h_t[char] += 1
        
        if h_s == h_t:
            return True
        else:
            return False

        