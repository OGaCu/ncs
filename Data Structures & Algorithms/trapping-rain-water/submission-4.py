class Solution:
    def trap(self, height: List[int]) -> int:
        maxWater = 0
        # BRUTE FORCE
        # water[i] = min(height[l], height[r]) - height[i]
        for i in range(len(height)):
            left = max(height[:i+1], default=0)
            right = max(height[i:], default=0)
            # left and right includes height[i]
            maxWater += min(left, right) - height[i]
        return maxWater
        