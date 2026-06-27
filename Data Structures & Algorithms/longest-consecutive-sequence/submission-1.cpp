class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // set.find() is O(logN)
        int longest = 0;
        set<int> s;
        for(const auto& num : nums) {
            s.insert(num);
        }
        for(const auto& num : nums) {
            if(s.find(num - 1) != s.end()) continue; // found prev
            // no prev found makes num the head of the seq
            bool cns = true;
            int longSoFar = 1;
            while(cns) {
                if(s.find(num + longSoFar) != s.end()) { // found next
                    longSoFar++;
                } else {
                    cns = false;
                }
            }
            longest = max(longest, longSoFar);
        }
        return longest;
    }
};
