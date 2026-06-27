class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // time O(number of strings * length of longest str)
        // space O(number of strings)
        unordered_map<string, vector<string>> res;
        for (const auto& str : strs) {
            vector<int> count(26, 0);
            // store frequency
            for(char c : str) {
                count[c - 'a']++;
            }
            // create map key
            string key = to_string(count[0]);
            for(int i = 1; i < 26; ++i) {
                key += "," + to_string(count[i]);
            }
            res[key].push_back(str);
        }
        // make output vector
        vector<vector<string>> result;
        for (const auto& pair : res) {
            result.push_back(pair.second);
        }
        return result;
    }
};
