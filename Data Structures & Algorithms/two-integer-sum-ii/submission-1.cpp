class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0; 
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
    }
};

// 1 3 4 6 7 9 target = 12
