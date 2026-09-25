class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = r_max = 0
        n = len(height)
        l_arr = [0] * n
        r_arr = [0] * n
       

        for i in range(n):
            j = -i - 1
            l_arr[i] = l_max
            r_arr[j] = r_max
            l_max = max(l_max, height[i])
            r_max = max(r_max, height[j])
        
        sum = 0
        for i in range(n):
            area = min(l_arr[i], r_arr[i])
            sum += max(0, area - height[i])
        

        return sum
        