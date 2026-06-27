class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // two pointers time O(n), space O(1)
        /* int start = 0; 
        int end = numbers.size() - 1;
        while(start < end) {
            if(numbers[start] + numbers[end] == target) {
                return {start + 1, end + 1};
            }
            while(numbers[start] + numbers[end] > target) {
                end--;
            }
            while(numbers[start] + numbers[end] < target) {
                start++;
            }
        }
        return {};
        */
        // hash map
        unordered_map<int, int> mp; 
        for (int i = 0; i < numbers.size(); ++i) {
            int tmp = target - numbers[i];
            if(mp.count(tmp)) {
                return {mp[tmp] + 1, i + 1};
            }
            mp[numbers[i]] = i;
        }
    }
};

// 1 3 4 6 7 9 target = 12
