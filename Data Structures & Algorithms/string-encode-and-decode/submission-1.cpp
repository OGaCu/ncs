class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        // # to differentiate length of str and actual str
        for (const auto& str : strs) {
            res += to_string(str.size()) + "#" + str;
        }
        return res;
    }

    vector<string> decode(string s) {
        // 3#cat10#hello
        // lc   lc
        vector<string> res;
        int curr = 0; 
        // substr(idxToStart, numChar)
        while (curr < s.size()) {
            int last = curr;
            while (s[curr] != '#') curr++;
            int len = stoi(s.substr(last, curr - last));
            res.push_back(s.substr(curr + 1, len));
            curr += len + 1;
        }
        return res;
    }
};
