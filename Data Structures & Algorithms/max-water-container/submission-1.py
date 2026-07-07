class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        area = 0
        for i, left in enumerate(heights):
            for j in range(i+1, len(heights)):
                right = heights[j]

                height = min(left, right)
                area = max(area, height * (j - i))

        return area