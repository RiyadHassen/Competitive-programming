class Solution:
    def trap(self, height: List[int]) -> int:
        max_min= []
        amount_of_water = 0
        global_max = -float('inf')
        for i in range(len(height)):
            if height[i] > global_max:
                global_max = height[i]
            max_min.append(global_max)
        global_max = -float('inf')
        for i in range(len(height)-1,-1,-1):
            if height[i] > global_max:
                global_max = height[i]
            if global_max < max_min[i]:
                max_min[i] =global_max
        for i in range(len(max_min)):
            amount_of_water += (max_min[i]-height[i])
        return amount_of_water
        