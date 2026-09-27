class Solution:
    def trap(self, height: List[int]) -> int:
        l_arr = [0] * len(height) 
        r_arr = [0] * len(height) 
        water = 0
        l_max = 0
        r_max = 0

        for l in range(len(height)):
            r = -l - 1
            l_arr[l] = l_max
            r_arr[r] = r_max

            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
        
        for i in range(len(l_arr)):
            potential = min(l_arr[i], r_arr[i])
            if potential < height[i]:
                continue
            
            water += potential - height[i]
        

        return water

            