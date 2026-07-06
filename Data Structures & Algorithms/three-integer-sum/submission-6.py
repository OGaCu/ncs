class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        # eliminates using duplicates 
        res = []
        nums.sort()
        # two sum
        # time O(n log n) + O(n^2)
        # space 
        for i, num in enumerate(nums):
            # avoid dup
            if i > 0 and nums[i-1] == num:
                continue
            # avoid only positives
            if num > 0:
                break
            # two sum
            l, r = i+1, len(nums) - 1
            while l < r:
                twoSum = nums[l] + nums[r]
                if -twoSum == num:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif -twoSum > num:
                    l += 1
                else:
                    r -= 1
        return res