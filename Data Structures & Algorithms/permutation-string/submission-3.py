class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window O(length of s2)
        size = len(s1)
        subset = Counter(s1)
        window = Counter(s2[:size]) # init window with first size char
        if subset == window:
            return True
            
        for i in range(size, len(s2)):
            
            window[s2[i]] += 1
            window[s2[i-size]] -= 1

            if window == subset:
                return True
            
            if window[s2[i - size]] == 0:
                del window[s2[i-size]] # keep window O(26) comparison

        return False