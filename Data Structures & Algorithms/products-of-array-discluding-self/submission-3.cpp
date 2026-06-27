class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // with division O(n) 
        /*
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
        */

        // without division using prefix & suffix
        // O(n) space
        /*
        int n = nums.size();
        vector<int> pre(n + 1);
        vector<int> post(n + 1);
        vector<int> res(n);
        pre[0] = 1;
        post[n - 1] = 1;
        // fill in prefix
        for (int i = 1; i < n; ++i) {
            pre[i] = pre[i - 1] * nums[i - 1];
        }
        for (int i = n - 2; i >= 0; --i) {
            post[i] = post[i + 1] * nums[i + 1];
        }
        for (int i = 0; i < n; ++i) {
            res[i] = pre[i] * post[i];
        }
        return res;
        */
        // optimal prefix & suffix O(1) space
        int n = nums.size();
        vector<int> res(n, 1);

        // calculate prefix
        for (int i = 1; i < n; ++i) {
            res[i] = res[i - 1] * nums[i - 1];
        }
        int postfix = 1;
        for(int i = n - 1; i >= 0; --i) {
            res[i] = res[i] * postfix;
            postfix *= nums[i];
        }
        return res;
    }
};
