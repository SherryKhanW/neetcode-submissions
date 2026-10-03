class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                stk_n, stk_i = stack.pop()
                res[stk_i] = i - stk_i

            stack.append((n, i))
        
        return res