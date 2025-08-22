class Solution:
    def partitionString(self, s: str) -> int:
        taken = {}
        windows = 1
        for x in s:
            if x in taken:
                windows += 1
                taken = {}
            taken[x] = 1
        return windows
