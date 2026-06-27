class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // brute force time O(n^2)
        /*
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
        */
        // two pointers O(n) time
        if(prices.empty()) return 0;
        int buy = 0;
        int sell = 1;
        int currMax = 0;
        // if l > r then negative profit: l++; r++
        // else positive profit r++;
        while (sell < prices.size()) {
            if(prices[buy] > prices[sell]) {
                buy = sell;
            }
            currMax = max(currMax, prices[sell] - prices[buy]);
            sell++;
        }
        return currMax;
    }
};
