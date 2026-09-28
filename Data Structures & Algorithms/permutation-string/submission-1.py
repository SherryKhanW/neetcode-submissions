class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n_1 = len(s1)
        n_2 = len(s2)

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        if n_1 > n_2:
            return False

        for i in range(n_1):
            count_s1[ord(s1[i]) - 97] += 1
            count_s2[ord(s2[i]) - 97] += 1

        if count_s1 == count_s2:
            return True
        
        for i in range(n_1, n_2):
            count_s2[ord(s2[i]) - 97] += 1
            count_s2[ord(s2[i - n_1]) - 97] -= 1

            if count_s1 == count_s2:
                return True
        
        return False
        

        
