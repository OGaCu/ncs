class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count; // count[num] = freq
        vector<vector<int>> freq(nums.size() + 1); // freq 0 to nums.size()
        for (int num : nums) {
            count[num]++;
        }
        for (const auto& entry : count) { // [num's freq] = num
            freq[entry.second].push_back(entry.first);
        }
        vector<int> res;
        for (int i = freq.size() - 1; i >= 0; --i) { // top freq num
            for (int num : freq[i]) {
                res.push_back(num);
                if(res.size() == k) return res;
            }
        }
        return res;
    }
};
