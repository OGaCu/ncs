class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0; 
        int right = heights.size() - 1;
        int res = 0;
        // O(n) time; O(1) space
        while (left < right) {
            int area = min(heights[left], heights[right]) * (right - left);
            res = max(area, res);
            // only move pointer with smaller height
            if(heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return res;
    }
};
