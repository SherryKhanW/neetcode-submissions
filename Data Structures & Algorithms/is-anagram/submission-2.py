class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case if length of s and t are not equal
        if len(s) != len(t):
            return False
            
        dict_1 = {}
        dict_2 = {}

        for i in s:
            if i in dict_1:
                dict_1[i] += 1
            else:
                dict_1[i] = 1

        for i in t:
            if i in dict_2:
                dict_2[i] += 1
            else:
                dict_2[i] = 1
        

        return dict_1 == dict_2