class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
            
        left_largest = [0] * n
        right_largest = [0] * n

        # 1. Build left_largest array
        max_l = 0
        for i in range(1, n):
            max_l = max(max_l, height[i-1])
            left_largest[i] = max_l

        # 2. Build right_largest array
        max_r = 0
        for i in range(n - 2, -1, -1):
            max_r = max(max_r, height[i+1])
            right_largest[i] = max_r # <-- Fixed: Assigned to the index!

        # 3. Calculate total trapped water
        max_area = 0
        for i, h in enumerate(height):
            limiting_height = min(left_largest[i], right_largest[i])
            my_area = limiting_height - h
            
            if my_area > 0:
                max_area += my_area

        return max_area