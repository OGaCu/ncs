class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation, use counter()
        from collections import Counter
        size = len(s1)
        subset = Counter(s1)

        for i in range(len(s2) - size + 1):
            permute = Counter(s2[i:i+size])
            if permute == subset:
                return True

        return False