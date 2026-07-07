class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # iterative binary search
        # time O(log n)
        # space O(1) where recursive is O(log n)
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid
        return -1