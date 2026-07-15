class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # O(2^n)
        # backtracking: Needed to undo choices (remove elements)
        # after exploring one branch of the decision tree
        res = []
        subset = []

        def dfs(i):  # i is the index of nums to explore
            if i == len(nums):
                res.append(subset.copy())
                return
            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # exclude nums[i], so basically append nothing
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
