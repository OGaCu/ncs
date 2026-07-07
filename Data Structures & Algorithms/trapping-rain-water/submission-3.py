class Solution:
    def trap(self, height: List[int]) -> int:
        maxWater = 0
        # BRUTE FORCE
        # water[i] = min(height[l], height[r]) - height[i]
        for i in range(len(height)):
            left = max(height[:i+1])
            right = max(height[i:])
            maxWater += min(left, right) - height[i]
        # print(max([], default=0))
        return maxWater
        