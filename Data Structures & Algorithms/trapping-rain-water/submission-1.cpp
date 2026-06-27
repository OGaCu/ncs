class Solution {
public:
    int trap(vector<int>& height) {
        // O(n) linear time, O(n) space
        // traverse to get max left
        // reverse to get max right
        // then find min(L, R)
        // calc: min(L, R) - height[i] >= 0
        int n = height.size();
        if(n == 0) return 0;
        vector<int> lMax(n), rMax(n);
        lMax[0] = height[0];
        for (int i = 1; i < n; ++i) {
            lMax[i] = max(lMax[i - 1], height[i]);
        }
        rMax[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            rMax[i] = max(rMax[i + 1], height[i]);
        }
        int res = 0;
        for (int i = 0; i < n; ++i) {
            cout << res << endl;
            res += min(lMax[i], rMax[i]) - height[i];
        }
        return res;

        // two pointers
        // O(n) linear time, O(n) space
        // int maxL = 0; int maxR = height.size() - 1
        // shift smaller max pointer bc otherwise spill


        // Brute force O(N^2 time)
        // if (height.empty()) return 0;

        // int n = height.size();
        // int res = 0;

        // for (int i = 0; i < n; ++i) {
        //     int leftMax = height[i];
        //     int rightMax = height[i];

        //     for (int j = 0; j < i; ++j) {
        //         leftMax = max(leftMax, height[j]);
        //     }

        //     for (int j = i; j < n; ++j) {
        //         rightMax = max(rightMax, height[j]);
        //     }

        //     res += min(leftMax, rightMax) - height[i];
        // }
        // return res;
    }
};
