class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window

        left = 0
        # window = {} # map key: char, value: freq
        from collections import Counter
        window = Counter()
        longest = 0
        right = 0

        while right < len(s):
            window[s[right]] += 1
            right += 1
            # out of k replacement then shrink window
            # window_size - maximum frequency character needs to be within k to be valid
            while (right - left) - window.most_common(1)[0][1] > k: # max char freq
                # remove the window[left] from map
                window[s[left]] -= 1
                left += 1
        
            longest = max(longest, right - left)
        return longest