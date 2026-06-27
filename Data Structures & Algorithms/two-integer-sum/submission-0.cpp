class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> comp; // complement, num index
        for(int i = 0; i < nums.size(); ++i) {
            auto it = comp.find(nums[i]);
            if(it != comp.end()) {
                return {it->second, i};
            } else {
                comp.insert({target - nums[i], i});
            }
        }
        return {}; // not reach

    }
};
