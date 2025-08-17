class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x
        while L <= R:
            mid = (L+R) // 2
            if mid * mid <= x:
                L = mid + 1
            else:
                R = mid - 1
        return L - 1
