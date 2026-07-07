class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BRUTE FORCE
        # area = 0
        # for i, left in enumerate(heights):
        #     for j in range(i+1, len(heights)):
        #         right = heights[j]

        #         height = min(left, right)
        #         area = max(area, height * (j - i))

        # return area

        # TWO POINTER
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            h = min(heights[l], heights[r])
            dist = r - l
            area = max(area, h * dist)
            
            if h == heights[l]: # left is lower then right height
                l += 1
            else:
                r -= 1

        return area