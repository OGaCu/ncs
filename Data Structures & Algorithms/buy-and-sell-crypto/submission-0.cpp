class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // two pointers O(n) time
        if(prices.empty()) return 0;
        int res = 0;
        for (int i = 0; i < prices.size(); ++i) {
            int buy = prices[i];
            for (int j = i + 1; j < prices.size(); ++j) {
                int sell = prices[j];
                res = max(sell - buy, res);
            }
        }
    
        return res;
    }
};
