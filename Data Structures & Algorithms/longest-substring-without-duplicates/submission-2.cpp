class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // brute force O(length of string * num of unique char)
        /*
        int res = 0;
        // abcaabcd
        for (int i = 0; i < s.length(); ++i) {
            unordered_set<char> charSet;
            for (int j = i; j < s.length(); ++j) {
                if(charSet.find(s[j]) != charSet.end()) break;
                charSet.insert(s[j]);
            }
            res = max(res, (int)charSet.size());
        }
        return res;
        */ 

        /*
        // sliding window, time O(n)
        if(s.empty()) return 0;
        int left = 0;
        int longest = 0;
        unordered_set<char> charSet;

        for (int r = 0; r < s.length(); ++r) {
            // found duplicates, move left of the window
            while(charSet.find(s[r]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }
            charSet.insert(s[r]);
            longest = max(longest, r - left + 1);
        }
        return longest;
        */

        // sliding window optimal
        unordered_map<char, int> mp; // char, last appeared idx 
        int l = 0, res = 0;
        
        for (int r = 0; r < s.length(); ++r) {
            if (mp.find(s[r]) != mp.end()) {
                l = max(mp[s[r]] + 1, l);
            }
            mp[s[r]] = r;
            res = max(res, r - l + 1);
        }
        return res;
    }
};
