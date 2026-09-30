class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1 = len(s1)
        S2 = len(s2)

        s1_chars = [0] * 26
        s2_chars = [0] * 26

        if S1 > S2:
            return False
        
        for i in range(S1):
            s1_chars[ord(s1[i]) - ord("a")] += 1
            s2_chars[ord(s2[i]) - ord("a")] += 1
        
        if s1_chars == s2_chars:
            return True
        
        for i in range(S1,S2):
            s2_chars[ord(s2[i]) - ord("a")] += 1
            s2_chars[ord(s2[i - S1]) - ord("a")] -= 1
        
            if s1_chars == s2_chars:
                return True
        

        return False
            
