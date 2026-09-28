class Solution:
    def minWindow(self, s: str, t: str) -> str:
        S, T = len(s), len(t)

        if S < T:
            return ""

        t_chars = {}
        window_chars = {}

        for c in t:
            t_chars[c] = 1 + t_chars.get(c, 0)

        min_window = 10**6
        start_index = -1

        l = 0
        have, need = 0, len(t_chars)

        for r in range(S):
            window_chars[s[r]]= 1 + window_chars.get(s[r], 0)

            if s[r] in t_chars and window_chars[s[r]] == t_chars[s[r]]:
                have += 1

            while have == need:
                w = r - l + 1
                
                if w < min_window:
                    start_index = l
                    min_window = w
                
                left_char = s[l]

                if left_char in t_chars and window_chars[left_char] == t_chars[left_char]:
                    have -= 1

                if window_chars[left_char] == 1: del window_chars[left_char]
                else: window_chars[left_char] -= 1

                l += 1
        
        if min_window == 10**6: return ""
        else: return s[start_index: start_index + min_window]
                

        
        
        


        