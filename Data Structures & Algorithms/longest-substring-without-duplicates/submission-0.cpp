class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // brute force O(length of string * num of unique char)
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
    }
};
