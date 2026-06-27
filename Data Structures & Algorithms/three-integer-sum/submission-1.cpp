class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // idx and all indexed nums are different
        // 3 sum equals to zero
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;

        for (int i = 0; i < nums.size(); ++i) {
            // smallest num is positive, impossible triplets from there
            if(nums[i] > 0) return res;
            // duplicates need to be avoided
            if(i > 0 && nums[i] == nums[i - 1]) continue;

            // two pointers for three sum
            int left = i + 1;
            int right = nums.size() - 1;
            while(left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == 0) {
                    res.push_back({nums[i], nums[left], nums[right]});
                    left++;
                    right--;
                    // prevent duplicates in two sum pointers
                    while(left < right && nums[left] == nums[left - 1]) left++;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return res;
    }
};
