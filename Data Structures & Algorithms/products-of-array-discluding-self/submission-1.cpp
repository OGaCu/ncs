class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int res = 1;
        int zeros = 0;
        for (const auto& num : nums) {
            if(num == 0) zeros++;
            else res *= num;
        }
        if (zeros > 1) return vector<int>(nums.size(), 0);
        vector<int> output(nums.size(), res);
        
        for (int i = 0; i < nums.size(); ++i) {
            if(zeros > 0 && nums[i] != 0) {
                output[i] = 0;
            } else if (nums[i] != 0){
                output[i] /= nums[i];
            }
        }
        return output;
    }
};
